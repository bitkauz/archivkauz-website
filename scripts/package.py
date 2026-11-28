from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parents[1]
public = root / "public"
out = root / "dist/archivkauz-website.zip"
out.parent.mkdir(exist_ok=True)
with ZipFile(out, "w", ZIP_DEFLATED) as archive:
    for file in sorted(public.rglob("*")):
        if file.is_file() and not file.is_symlink():
            archive.write(file, file.relative_to(public).as_posix())
with ZipFile(out) as archive:
    assert archive.testzip() is None
    assert "index.html" in archive.namelist()
    assert "en/index.html" in archive.namelist()
    assert "updates/index.html" in archive.namelist()
    assert "en/updates/index.html" in archive.namelist()
print(out)
