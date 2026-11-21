#!/usr/bin/env python3
"""Prüft trip.json auf Tippfehler und kaputte Verweise.

Aufruf im Repo-Ordner:  python3 tools/check.py
"""
import json
import sys
from pathlib import Path

ARTEN = {"arr", "fl", "car", "loc", "tr", "sk", "dep"}
LABELS = {"l", "r", "t", "b"}

path = Path(__file__).resolve().parent.parent / "trip.json"
try:
    T = json.loads(path.read_text(encoding="utf-8"))
except json.JSONDecodeError as e:
    sys.exit(f"trip.json ist kein gültiges JSON: Zeile {e.lineno}, Spalte {e.colno}: {e.msg}")

fehler, warn = [], []
orte, tage, hotels = T.get("orte", {}), T.get("tage", []), T.get("hotels", [])

for k, o in orte.items():
    for f in ("jp", "name", "lat", "lon"):
        if f not in o:
            fehler.append(f"Ort {k}: Feld '{f}' fehlt")
    if not (30 < o.get("lat", 0) < 46 and 128 < o.get("lon", 0) < 146):
        fehler.append(f"Ort {k}: Koordinaten liegen nicht in Japan ({o.get('lat')}, {o.get('lon')})")
    if o.get("label", "r") not in LABELS:
        fehler.append(f"Ort {k}: label muss l, r, t oder b sein")
    for c in ("kultur", "essen", "trinken"):
        for x in o.get(c, []):
            if not x.get("text"):
                fehler.append(f"Ort {k}/{c}: Eintrag ohne text")
            if not x.get("maps"):
                warn.append(f"Ort {k}/{c}: '{x.get('text', '')[:40]}' ohne maps-Suchbegriff")

prev = None
for t in tage:
    n = t.get("tag")
    if prev is not None and n != prev + 1:
        warn.append(f"Tag {n}: folgt nicht direkt auf Tag {prev}")
    prev = n
    if t.get("art") not in ARTEN:
        fehler.append(f"Tag {n}: art '{t.get('art')}' unbekannt, erlaubt: {', '.join(sorted(ARTEN))}")
    for s in t.get("stopps", []):
        if s not in orte:
            fehler.append(f"Tag {n}: Stopp '{s}' gibt es nicht unter 'orte'")
    h = t.get("hotel")
    if h is not None and not (0 <= h < len(hotels)):
        fehler.append(f"Tag {n}: hotel {h} existiert nicht (0 bis {len(hotels) - 1})")
    for f in ("titel", "wochentag", "plan"):
        if not t.get(f):
            fehler.append(f"Tag {n}: Feld '{f}' fehlt oder ist leer")

for i, h in enumerate(hotels):
    if h.get("ort") not in orte:
        fehler.append(f"Hotel {i} ({h.get('stadt')}): ort '{h.get('ort')}' gibt es nicht")
    n = sum(1 for t in tage if t.get("hotel") == i)
    if n != h.get("anzahlNaechte"):
        warn.append(f"Hotel {i} ({h.get('stadt')}): anzahlNaechte={h.get('anzahlNaechte')}, aber {n} Tage verweisen darauf")
    if h.get("preisMin", 0) > h.get("preisMax", 0):
        fehler.append(f"Hotel {i}: preisMin größer als preisMax")

for w in warn:
    print("Hinweis:", w)
for f in fehler:
    print("FEHLER: ", f)
print(f"\n{len(orte)} Orte, {len(tage)} Tage, {len(hotels)} Hotels geprüft: "
      f"{len(fehler)} Fehler, {len(warn)} Hinweise.")
sys.exit(1 if fehler else 0)
