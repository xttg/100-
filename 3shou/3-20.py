import pandas as pd
import re

pat = re.compile("Category")
df = pd.read_json("jawiki-country.json",orient="records",lines=True)
british = df[df["title"]=="イギリス"]["text"].values
print(british[0])
