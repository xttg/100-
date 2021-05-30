import pandas as pd
import re

country = pd.read_json("jawiki-country.json", orient="records", lines=True)
britain = country[country["title"] == "イギリス"]["text"].values

text_lines = britain[0].split("\n")

pat = re.compile(r"\|(.+?)\s=\s*(.+)")
empha = re.compile(r"\'{2,5}(.+?)\'{2,5}")
link = re.compile(r"\[\[(.+?)\]\]")
html = re.compile(r"<(.+?)>")


d = {}

for line in text_lines:
    ans = re.search(pat, line)
    if ans:
        d[ans[1]] = ans[2]
    text = re.sub(empha, "\\1", line)
    text1 = re.sub(link, "\\1", text)
    text2 = re.sub(html, "", text1)
    print(text2)
print(d)
