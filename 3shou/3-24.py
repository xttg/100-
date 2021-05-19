import pandas as pd
import re

country = pd.read_json("jawiki-country.json", orient="records", lines=True)
britain = country[country["title"] == "イギリス"]["text"].values
text_lines = britain[0].split("\n")

pat = re.compile("File|ファイル:(.+?)\|")

for line in text_lines:
    media = re.findall(pat, line)
    if len(media):
        print(*media, sep="\n")
