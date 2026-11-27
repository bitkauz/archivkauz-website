# ArchivKauz – Produktwebsite

Offizielle geplante Produktadresse: **https://archivkauz.bitkauz.de/**. Eigenständige DE/EN-Website von Bitkauz, getrennt von der Anwendung und dem privaten Lizenzserver.

- Anwendung und Dokumentation: https://github.com/bitkauz/archivkauz
- Lizenzportal und Lizenz-API: https://license.bitkauz.de/ (geplant; eigenständiger Dienst)
- Status: Statische Website im Repository, kein nachgewiesener Livebetrieb. Logoentwurf, rechtliche Hinweise und Hostingfreigabe sind vor Veröffentlichung zu prüfen.

## Struktur

- `public/`: vollständiger Webroot, HTML/CSS und lokale SVG-Assets
- `public/en/`: englische Sprachfassung
- `docs/BRAND.md`: Markenentwurf
- `docs/DEPLOYMENT.md`: Webspace und Release-Ablauf
- `scripts/`: lokale Linkprüfung und flaches ZIP

## Vorschau
`python3 -m http.server 8000 --directory public` — http://localhost:8000/. Keine Buildpflicht.

## Build und Auslieferung
`python3 scripts/check_site.py` prüft lokale Verweise und SVG-Dateien. `python3 scripts/package.py` erzeugt `dist/archivkauz-website.zip` mit `index.html` unmittelbar im Archiv-Root. Die Action erzeugt ein ZIP-Artefakt, bei Versions-Tags zusätzlich ein GitHub Release. Keine ungefragte FTP-Veröffentlichung oder Übermittlung von Zugangsdaten.

## Projektstatus
Die Website beschreibt ausschließlich geplante Funktionen. Keine installierbare ArchivKauz-Version und kein aktiver Lizenzdienst werden behauptet. Für rechtliche Projektinformationen siehe die Dokumentation der Anwendung; Softwarelizenz/CLA stehen noch aus.
