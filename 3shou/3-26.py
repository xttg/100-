import pandas as pd
import re

country = pd.read_json("jawiki-country.json", orient="records", lines=True)
britain = country[country["title"] == "イギリス"]["text"].values
text_lines = britain[0].split("\n")

d = {}

pat = re.compile("\|(.+?)\s=\s*(.+)")
empha = re.compile("\'{2,5}")

for line in text_lines:
    ans = re.search(pat, line)
    if ans:
        d[ans[1]] = ans[2]
    text = re.sub(empha, "", line)
    print(text)
print(d)
