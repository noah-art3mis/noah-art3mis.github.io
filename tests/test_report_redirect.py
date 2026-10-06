"""Run with uv run --no-project python -m unittest discover -s tests -q."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import shutil
import subprocess
import tempfile
from threading import Thread
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PreviewHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split('?', 1)[0] == '/obras-df/':
            content = b'''<!doctype html><output id="destination"></output>
<script>document.querySelector('output').textContent = location.pathname + location.search + location.hash;</script>'''
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content)
            return
        super().do_GET()

    def log_message(self, *args):
        pass


class PublishedReportRedirectTest(unittest.TestCase):
    def test_old_report_links_keep_query_and_section(self):
        chrome = shutil.which('google-chrome') or shutil.which('chromium')
        self.assertIsNotNone(chrome, 'Install Chrome or Chromium to verify redirects')
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(PreviewHandler, directory=ROOT))
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            for old_path in ('/takehome-lablivre-analysis/', '/takehome-lablivre-analysis/index.html'):
                with self.subTest(old_path=old_path), tempfile.TemporaryDirectory() as profile:
                    url = f'http://127.0.0.1:{server.server_port}{old_path}?from=cv#4.-Resumo-executivo'
                    result = subprocess.run(
                        [chrome, '--headless=new', '--no-sandbox', '--disable-gpu',
                         f'--user-data-dir={profile}', '--virtual-time-budget=2000', '--dump-dom', url],
                        capture_output=True, text=True, timeout=30, check=True,
                    )
                    self.assertIn(
                        '<output id="destination">/obras-df/?from=cv#4.-Resumo-executivo</output>',
                        result.stdout,
                    )
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == '__main__':
    unittest.main()
