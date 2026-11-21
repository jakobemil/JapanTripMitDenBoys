# Japan-Trip mit den Boys · 8.–25. März 2027

Interaktive Reiseübersicht: Karte mit Zeitstrahl, Tagespläne, Orts-Highlights (Kultur, Essen, Trinken) mit Google-Maps-Links, Transport, Hotels, Onsen mit Tattoos, Budget-Rechner und Checkliste.

## Aufbau

| Datei | Inhalt |
|---|---|
| `trip.json` | **Alle Reisedaten.** Hier wird geändert. |
| `index.html` | Darstellung: liest `trip.json` und zeigt Karte, Zeitstrahl und Tabellen. Muss bei Routenänderungen nicht angefasst werden. |
| `tools/check.py` | Prüft `trip.json` auf Tippfehler und kaputte Verweise. |

Es gibt keinen Build-Schritt. Karte: Leaflet mit Kacheln von Esri und OpenStreetMap.

## Daten ändern

1. `trip.json` bearbeiten (direkt auf GitHub mit dem Stift-Symbol oder lokal).
2. Prüfen: `python3 tools/check.py`
3. Committen und pushen, Netlify oder Cloudflare veröffentlicht automatisch.

### Die wichtigsten Bereiche in `trip.json`

**`orte`**: jeder Ort mit Kürzel als Schlüssel, z. B. `"BEP"` für Beppu.

```json
"BEP": {
  "jp": "別府", "name": "Beppu", "lat": 33.28, "lon": 131.49,
  "label": "r",
  "kultur":  [{ "text": "Takegawara Onsen, Badehaus von 1938", "maps": "Takegawara Onsen" }],
  "essen":   [{ "text": "Toriten, Oitas Hähnchen-Tempura", "maps": "Toyotsune Beppu" }],
  "trinken": [{ "text": "Izakaya um Kitahama", "maps": "Kitahama Beppu" }]
}
```

- `label`: Seite der Beschriftung auf der Karte, `l` links, `r` rechts, `t` oben, `b` unten.
- `maps`: Suchbegriff für den Google-Maps-Knopf, am besten der englische Name.
- `klein: true`: Ort wird auf dem Handy in der Gesamtansicht nicht beschriftet.
- Koordinaten: in Google Maps rechtsklicken, die erste Zahl ist `lat`, die zweite `lon`.

**`tage`**: ein Eintrag pro Reisetag, in Reihenfolge.

```json
{
  "tag": 12, "wochentag": "Fr", "region": "Yamaguchi",
  "titel": "Kanmon-Straße, Fischmarkt und Torii an der Klippe",
  "art": "car",
  "stopps": ["BEP", "KAN", "TSU", "MOT", "NAG"],
  "tags": ["Auto ~260 km", "Langer Tag"],
  "plan": ["Erster Punkt", "Zweiter Punkt"],
  "essen": "…", "abseits": "…",
  "uebernachtung": "Nagato Yumoto, 1 Nacht",
  "hotel": 3
}
```

- `art`: `car` Mietwagen, `tr` Zug/Fähre, `sk` Shinkansen, `fl` Flug, `loc` vor Ort, `arr` Ankunft, `dep` Abreise. Bestimmt Linie und Farbe.
- `stopps`: Ort-Kürzel aus `orte`, in Fahrtreihenfolge. Daraus wird die Linie auf der Karte.
- `tags`: Chips im Tag. Ein Tag mit „Auto “ wird rot, „Autofrei“ rosa.
- `hotel`: Nummer des Hotels in `hotels` (gezählt ab 0), `null` ohne Übernachtung.

**`hotels`**: `ort` (Kürzel), `naechte`, `stadt`, `empfehlung`, `alternativen`, `preis` (Text), `hinweis`, `preisMin`/`preisMax` in Yen pro Nacht für den Budget-Rechner, `anzahlNaechte`.

**Weitere Bereiche:** `transport`, `mietwagen`, `onsen`, `essenTabelle`, `budget` (`art`: `person`, `auto` oder `hotels`), `checkliste`, `quellen`, `reise` (Personen und Wechselkurs als Startwerte).

### Beispiel: Ort einfügen
Einen Abstecher nach Kobe am 18. März: unter `orte` einen Eintrag `"KOB"` mit Koordinaten anlegen und am Tag 18 die Stopps auf `["KUR", "HIM", "KOB", "OSA"]` ändern. Mehr braucht es nicht.

## Lokal ansehen

Weil die Seite `trip.json` nachlädt, funktioniert ein Doppelklick auf `index.html` nicht, der Browser blockiert das. Stattdessen im Repo-Ordner:

```bash
python3 -m http.server 8000
```

und dann http://localhost:8000 öffnen.

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

`trip.json` bearbeiten und pushen. Netlify und Cloudflare veröffentlichen jeden Push auf `main` automatisch neu.
