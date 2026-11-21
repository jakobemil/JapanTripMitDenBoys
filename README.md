# Japan-Trip mit den Boys · 8.–25. März 2027

Interaktive Reiseübersicht: Karte mit Zeitstrahl, Tagespläne, Orts-Highlights (Kultur, Essen, Trinken) mit Google-Maps-Links, Transport, Hotels, Onsen mit Tattoos, Budget-Rechner und Checkliste.

Die ganze Seite ist eine einzige Datei: `index.html`. Es gibt keinen Build-Schritt und keine Abhängigkeiten. Karte: Leaflet mit Kartenkacheln von Esri und OpenStreetMap, beides wird im Browser geladen.

## Lokal ansehen

`index.html` herunterladen und direkt in Chrome, Safari oder Firefox öffnen (Internet nötig, nicht in einer Datei-Vorschau öffnen).

## Online stellen (Repo bleibt privat)

### Variante A: Netlify (am schnellsten)
1. Auf https://app.netlify.com anmelden (mit GitHub).
2. **Add new site → Import an existing project → GitHub** → `jakobemil/JapanTripMitDenBoys` wählen.
3. Build command leer lassen, Publish directory `.` (steht schon in `netlify.toml`).
4. **Deploy**. Unter *Site configuration → Change site name* einen Namen vergeben, z. B. `japan-boys-2027` → `https://japan-boys-2027.netlify.app`.

Die Seite ist für jeden mit Link erreichbar. Ein Passwortschutz kostet bei Netlify extra.

### Variante B: Cloudflare Pages mit Zugangsschutz (nur eingeladene Leute)
1. Auf https://dash.cloudflare.com → **Workers & Pages → Create → Pages → Connect to Git** → Repo wählen.
2. Framework preset: *None*, Build command leer, Build output directory `/`.
3. **Save and Deploy** → Adresse `https://<name>.pages.dev`.
4. Zugriff beschränken: im Pages-Projekt unter **Settings → Access policy** (bzw. Zero Trust → Access → Applications) eine Policy anlegen, „Emails“ mit den Adressen der Mitreisenden. Wer die Seite öffnet, bekommt dann einen Code per E-Mail. Kostenlos bis 50 Nutzer.

### Variante C: GitHub Pages
Nur mit öffentlichem Repo (GitHub Free) oder GitHub Pro. Settings → Pages → Branch `main`, Ordner `/ (root)`.

## Suchmaschinen

`robots.txt`, `_headers`, `netlify.toml` und ein Meta-Tag sagen Suchmaschinen, dass sie die Seite nicht indexieren sollen. Das ist kein Schutz, aber die Seite taucht so nicht bei Google auf.

## Änderungen

`index.html` bearbeiten und pushen. Netlify und Cloudflare veröffentlichen jeden Push auf `main` automatisch neu.
