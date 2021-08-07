
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import confusion_matrix
vectorizer = CountVectorizer()

train_df = pd.read_csv("feature/train.txt", sep='\t', header=0)
valid_df = pd.read_csv("feature/valid.txt", sep='\t', header=0)
test_df = pd.read_csv("feature/test.txt", sep='\t', header=0)

# fitで単語->IDの対応を決定。transformで 実際に単語をIDに変換。(文番号、単語のID),単語の数
X_train = vectorizer.fit_transform(train_df['TITLE'])
X_valid = vectorizer.transform(valid_df['TITLE'])
X_test = vectorizer.transform(test_df['TITLE'])

clf = LogisticRegression(max_iter=200)
# 訓練データのtitleをencodingしたリスト（入力）および正解ラベル（カテゴリ）を使って重みを学習
clf.fit(X_train, train_df['CATEGORY'])

dic = {'b': 'business', 't': 'science and technology',
       'e': 'entertainment', 'm': 'health'}


def predict(text):
    X = vectorizer.transform(text)  # transformで回帰モデルに入力できるベクトルに変換
    ls_proba = clf.predict_proba(X)
    for proba in ls_proba:
        for c, p in zip(clf.classes_, proba):
            print(dic[c]+":", p)


y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)  # モデルの予測したカテゴリ

y_train = train_df['CATEGORY']
y_test = test_df['CATEGORY']  # 正解ラベル

names = np.array(vectorizer.get_feature_names())
labels = ['b', 't', 'e', 'm']

for c, coef in zip(clf.classes_, clf.coef_):
    idx = np.argsort(coef)[::-1]
    print(dic[c])
    print(names[idx][:10])  # 重みの高い特徴量トップ10
    print(names[idx][-10:][::-1])  # 重みの低い特徴量トップ10
