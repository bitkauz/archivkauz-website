# ArchivKauz – Produktwebsite

[![Website prüfen und paketieren](https://github.com/bitkauz/archivkauz-website/actions/workflows/website.yml/badge.svg)](https://github.com/bitkauz/archivkauz-website/actions/workflows/website.yml)

Offizielle geplante Produktadresse: **https://archivkauz.bitkauz.de/**. Eigenständige DE/EN-Website von Bitkauz, getrennt von der Anwendung und dem privaten Lizenzserver.

- Anwendung: separates privates Entwicklungsrepository; keine öffentlichen Kernpakete.
- Lizenzportal und Lizenz-API: eigenständiger Dienst; produktive Kundenfunktionen noch nicht freigegeben.
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
Stand 27.11.2026: interne Alpha `0.1.0-alpha.1-dev.3` mit ersten Sammlungsfunktionen; produktive Aktivierung und Installation noch nicht freigegeben. Die Website trennt intern umgesetzte Funktionen, nächste Schritte und geplante Erweiterungen. Lizenzmodell: proprietäre, lizenzpflichtige Self-Hosting-Software; keine öffentliche Ausgabe des Anwendungskerns. Preise, Nutzungsbedingungen und öffentlicher Download bleiben bis zur Freigabe offen.
