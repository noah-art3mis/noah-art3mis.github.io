"""Checks what AI readers get from the built site.

Build the site first, then run with:
SITE_DIR=path/to/_site uv run --no-project python -m unittest tests.test_llms_visibility -q
"""

import os
from pathlib import Path
import re
import unittest


SITE = Path(os.environ.get('SITE_DIR', '_site'))


def read(path):
    return (SITE / path).read_text(encoding='utf-8')


class MarkdownRoutesTest(unittest.TestCase):
    def test_home_is_clean_markdown(self):
        markdown = read('index.md')
        self.assertTrue(markdown.startswith('# Gustavo Costa\n'))
        self.assertIn('## Selected research & projects', markdown)
        self.assertIn('**Lead Engineer, LLM Systems & Research Infrastructure**', markdown)
        self.assertIn('2026 – present', markdown)
        self.assertIn('[All projects](/projects.md)', markdown)
        self.assert_clean(markdown)

    def test_projects_is_clean_markdown(self):
        markdown = read('projects.md')
        self.assertTrue(markdown.startswith('# All Projects\n\n'))
        self.assertIn('### Technical', markdown)
        self.assertNotIn('permalink:', markdown)
        self.assert_clean(markdown)

    def test_pages_advertise_their_markdown(self):
        for page, route in (('index.html', '/index.md'), ('projects/index.html', '/projects.md')):
            with self.subTest(page=page):
                self.assertIn(f'<link rel="alternate" type="text/markdown" href="{route}">', read(page))

    def assert_clean(self, markdown):
        self.assertNotRegex(markdown, r'\{:', 'Kramdown attributes are for the HTML only')
        self.assertNotRegex(markdown, r'</?[a-z][^>]*>', 'no leftover HTML')
        self.assertNotRegex(markdown, r'\n\s*\n\s*\n', 'no runs of blank lines')
        self.assertEqual(len(re.findall(r'^# ', markdown, re.M)), 1, 'one h1')


class HtmlTest(unittest.TestCase):
    def test_every_page_has_one_h1(self):
        for page in ('index.html', 'projects/index.html'):
            with self.subTest(page=page):
                self.assertEqual(read(page).count('<h1'), 1)

    def test_canonical_url_is_the_real_domain(self):
        self.assertIn('<link rel="canonical" href="https://simulacro.cv/"', read('index.html'))
        self.assertNotIn('noah-art3mis.github.io', read('index.html'))


class ConventionFilesTest(unittest.TestCase):
    def test_robots_signals_search_live_ai_use_and_training(self):
        self.assertEqual(
            read('robots.txt'),
            'User-agent: *\nContent-Signal: search=yes, ai-input=yes, ai-train=yes\nDisallow:\n',
        )

    def test_llms_txt_is_well_formed_linked_and_its_links_resolve(self):
        llms = read('llms.txt')
        self.assertRegex(llms, r'^# Gustavo Costa\n\n> \S')
        links = re.findall(r'\]\((/[^)]+)\)', llms)
        self.assertIn('/index.md', links)
        self.assertIn('/projects.md', links)
        for link in links:
            self.assertTrue((SITE / link.lstrip('/')).exists(), link)
        self.assertIn('href="/llms.txt"', read('index.html'))


if __name__ == '__main__':
    unittest.main()
