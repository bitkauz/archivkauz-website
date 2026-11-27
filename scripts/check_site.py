from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree

root = Path(__file__).resolve().parents[1] / "public"

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.h1 = 0
        self.lang = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "html":
            self.lang = attrs.get("lang")
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        self.links.extend(attrs[k] for k in ("href", "src") if attrs.get(k))

pages = {}
for file in sorted(root.rglob("*.html")):
    page = Page()
    page.feed(file.read_text(encoding="utf-8"))
    assert page.h1 == 1 and page.lang in ("de", "en"), file
    pages[file.resolve()] = page
assert (root / "index.html").resolve() in pages and (root / "en/index.html").resolve() in pages
for file, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme in ("https", "mailto"):
            continue
        assert not url.scheme and not url.netloc, f"Unexpected link: {link}"
        target = (file.parent / unquote(url.path)).resolve() if url.path else file
        assert target.is_relative_to(root.resolve()), link
        if target.is_dir():
            target = target / "index.html"
        assert target.is_file(), f"Broken local link: {file}: {link}"
        if url.fragment:
            assert target in pages and unquote(url.fragment) in pages[target].ids, link
for file in root.rglob("*.svg"):
    ElementTree.parse(file)
print(f"OK: {len(pages)} pages, local links, anchors and SVG assets")
