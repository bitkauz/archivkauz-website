# Veröffentlichung auf dem eigenen Webspace

Vorgesehener Host: archivkauz.bitkauz.de. Domain und TLS durch den Betreiber einrichten; dieses Repository enthält keine Hostingzugangsdaten und führt keine Veröffentlichung durch.

1. Subdomain im Hostingpanel anlegen, eigenen Webroot zuweisen und HTTPS einrichten.
2. Impressums-/Datenschutzinformationen und Markenentwurf vor dem ersten öffentlichen Livebetrieb prüfen und ergänzen. Keine unfertigen Downloadlinks oder Lizenzfreigaben.
3. Im Repository unter Actions den Workflow „Website prüfen und paketieren“ ausführen. Das Artefakt herunterladen und das enthaltene flache ZIP entpacken; alternativ lokal bauen.
4. Inhalt des ZIP (index.html, en/, updates/, assets/) in den Webroot übertragen, keine zusätzliche Verzeichnisebene.
5. DE/EN, Navigation, Logo, TLS und öffentliche Links (keine Links auf private Repositories) prüfen.
6. Bei freigegebenem Versions-Tag v* erzeugt die Action einen Release mit ZIP. Vor einem Update bisherige Website sichern, neue Version getrennt testen, dann umschalten.

Die bisherige GitHub-Pages-Planung ist abgelöst; keine automatische Pages- oder FTP-Veröffentlichung. Der Lizenzdienst läuft separat; diese statische Website übermittelt keine Besucherinformationen an ihn. Die öffentliche Kundenfunktion wird erst nach Freigabe verlinkt. Installations- und Lizenzmeldungen der späteren Anwendung sind getrennt davon und werden vor Freigabe transparent dokumentiert.
