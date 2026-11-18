"""Write a copy of index.html into each tab's folder so erichl.com/records/ etc. load directly.

Edit only index.html, then run `python build.py` before pushing.
"""
from pathlib import Path

TABS = ["photography", "projects", "likes", "records"]
root = Path(__file__).parent
page = (root / "index.html").read_text(encoding="utf-8")

for tab in TABS:
    url = f"https://erichl.com/{tab}/"
    out = page.replace('<meta property="og:url" content="https://erichl.com/">',
                       f'<meta property="og:url" content="{url}">')
    (root / tab).mkdir(exist_ok=True)
    (root / tab / "index.html").write_text(out, encoding="utf-8")
    print(f"wrote {tab}/index.html")
