from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
vectorizer = CountVectorizer()

train_df = pd.read_csv("feature/train.txt", sep='\t', header=0)
valid_df = pd.read_csv("feature/valid.txt", sep='\t', header=0)
test_df = pd.read_csv("feature/test.txt", sep='\t', header=0)

X_train = vectorizer.fit_transform(train_df['TITLE'])
X_valid = vectorizer.transform(valid_df['TITLE'])
X_test = vectorizer.transform(test_df['TITLE'])

clf = LogisticRegression(max_iter=200)
clf.fit(X_train, train_df['CATEGORY'])  # 訓練データのタイトル（入力）および正解ラベル（カテゴリ）

dic = {'b': 'business', 't': 'science and technology',
       'e': 'entertainment', 'm': 'health'}


def predict(text):
    X = vectorizer.transform(text)  # transformで回帰モデルに入力できるベクトルに変換
    ls_proba = clf.predict_proba(X)
    for proba in ls_proba:
        for c, p in zip(clf.classes_, proba):
            print(dic[c]+":", p)


s = [train_df.iloc[1]['TITLE']]
print(s)
predict(s)
