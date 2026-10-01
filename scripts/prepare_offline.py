"""Version the offline cache from the exact public guide files (standard library only)."""
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = ['index.html', 'manifest.webmanifest', 'icons/guide-192.png', 'icons/guide-512.png']


def main():
    digest = sha256()
    for name in PUBLIC_FILES:
        digest.update(name.encode('utf-8'))
        digest.update(b'\0')
        digest.update((ROOT / name).read_bytes())
    worker = ROOT / 'sw.js'
    replacement = f"const CACHE='daikin-guide-{digest.hexdigest()[:16]}'"
    content, count = re.subn(r"const CACHE='daikin-guide-[^']+'", replacement, worker.read_text(), count=1)
    if count != 1:
        raise SystemExit('Could not locate the offline cache version in sw.js')
    worker.write_text(content)
    print('Prepared offline guide release:', digest.hexdigest()[:16])


if __name__ == '__main__':
    main()
