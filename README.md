# Casteel Daikin Guide

A static field reference for Daikin, Goodman, Amana, and documented EWC equipment. Manufacturer reference card contents and the embedded AHRI catalog remain the source for service information.

## Offline and installation

Open the hosted guide online once and wait for **Saved for offline use**. It can then reopen without a connection, including reference search and the embedded AHRI lookup. External manufacturer documents are not downloaded automatically.

Compatible browsers offer **Install guide**. On iPhone/iPad Safari, use Share → Add to Home Screen. When a newer saved release is available, **Update guide** activates it and reloads the app. The single HTML file also remains usable when downloaded and opened locally.

The visible reference compilation date comes from `data/daikin-reference/00-README-rules-and-contents.md`; the AHRI date identifies its embedded catalog snapshot. Publishing a code update does not imply the manufacturer information has been reviewed again.

## Local development and deployment

```sh
python3 scripts/prepare_offline.py
python3 -m http.server 8000
```

Open `http://localhost:8000`. Service workers require HTTPS or localhost. Netlify runs the cache-version script before publishing, so any guide, manifest, or icon change produces a new offline release. `/data/*` remains blocked by the existing Netlify rule.

## Regression checks

```sh
python3 -m pip install -r tests/requirements.txt
python3 -m playwright install chromium
python3 -m unittest discover -s tests -v
```

Tests run against a temporary copy of the site, including the offline update test; they do not alter service data or application files.
