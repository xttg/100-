import pandas as pd
import re
import requests

country = pd.read_json("jawiki-country.json", orient="records", lines=True)
britain = country[country["title"] == "イギリス"]["text"].values

text_lines = britain[0].split("\n")

pat = re.compile(r"\|(.+?)\s=\s*(.+)")

d = {}

for line in text_lines:
    ans = re.search(pat, line)
    if ans:
        d[ans[1]] = ans[2]

S = requests.Session()
URL = "https://commons.wikimedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "File:" + d["国旗画像"],
    "prop": "imageinfo",
    "iiprop": "url"
}
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA["query"]["pages"]
for k, v in PAGES.items():
    print(v["imageinfo"][0]["url"])
