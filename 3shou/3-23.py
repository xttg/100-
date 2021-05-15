import pandas as pd
import re

pat=re.compile("^=+.*=+$")
df = pd.read_json("jawiki-country.json",orient="records",lines=True)
british = df[df["title"]=="イギリス"]["text"].values

lines_list = british[0].split("\n")

for line in lines_list:
    if re.search(pat,line):
        level=line.count("=")//2-1
        print(line.replace("=",""),level)
