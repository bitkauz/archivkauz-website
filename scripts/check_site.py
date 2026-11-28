from pathlib import Path
from html.parser import HTMLParser
import re
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
versions = set()
for required, lang in (("index.html", "de"), ("en/index.html", "en"), ("updates/index.html", "de"), ("en/updates/index.html", "en")):
    assert (root / required).resolve() in pages, required
    assert pages[(root / required).resolve()].lang == lang, required
    source = (root / required).read_text(encoding="utf-8")
    current = re.findall(r"<strong>(\d+\.\d+\.\d+-alpha\.\d+-dev\.\d+)</strong>", source)
    assert len(current) == 1, f"Missing or ambiguous current alpha version: {required}"
    versions.add(current[0])
    assert not re.search(r"github\.com/bitkauz/(?:archivkauz|bitkauz-license-server)(?=[/\s\"\x27]|$)", source), f"Private repository link: {required}"
assert len(versions) == 1, "Development version differs between languages or news pages"
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
