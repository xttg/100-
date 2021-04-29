import re
with open("popular-names.txt","r") as f:
    before=f.read()
    after=re.sub("[\t]"," ",before)
with open("2-11data.txt","w") as d:#新規ファイルを作成してtab→spaceにしたものを書き込む
    d.write(after)
