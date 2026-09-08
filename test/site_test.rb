require 'minitest/autorun'
require 'nokogiri'
require 'uri'

class SiteTest < Minitest::Test
  ROOT = File.expand_path('../_site', __dir__)

  def page(path)
    Nokogiri::HTML(File.read(File.join(ROOT, path)))
  end

  def test_home_has_a_readable_document_outline
    document = page('index.html')
    assert_equal 1, document.css('main h1').length, 'Home needs one main heading'
    assert document.at_css('a[href="#main-content"]'), 'Keyboard users need a skip link'
  end

  def test_project_links_have_destinations
    links = page('projects/index.html').css('main a')
    broken = links.select { |link| link['href'].to_s.strip.empty? || link['href'] == '#' }
    assert_empty broken.map(&:text), 'Project names must not be empty links'
  end

  def test_not_found_page_offers_a_way_home
    document = page('404.html')
    assert document.at_css('main a[href="/"]'), '404 content needs a recovery link'
  end

  def test_local_links_and_assets_resolve_in_the_built_site
    %w[index.html projects/index.html 404.html].each do |path|
      page(path).css('a[href], img[src], link[rel="stylesheet"]').each do |element|
        target = element['href'] || element['src']
        next if target.to_s.empty? || target.start_with?('#', '//')
        uri = URI.parse(target)
        next if uri.scheme
        relative = uri.path.sub(%r{\A/}, '')
        file = File.join(ROOT, relative)
        file = File.join(file, 'index.html') if File.directory?(file)
        assert File.file?(file), "#{path}: missing #{target}"
      end
    end
  end
end
