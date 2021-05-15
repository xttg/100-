import pandas as pd
import re

pat = re.compile("Category")
df = pd.read_json("jawiki-country.json",orient="records",lines=True)
british = df[df["title"]=="イギリス"]["text"].values

lines_list = british[0].split("\n")

for line in lines_list:
    if re.search(pat,line):
        line = line.replace("[[","").replace("|元","").replace("Category:","").replace("|*","").replace("]]","")
        print(line)
