
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import itertools
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
y_valid = valid_df['CATEGORY']
y_test = test_df['CATEGORY']  # 正解ラベル


def calc_scores(c, solver, class_weight):
    clf = LogisticRegression(
        C=c, max_iter=1000, solver=solver, class_weight=class_weight)  # 正則化パラメータを変えたモデル
    clf.fit(X_train, y_train)

    y_train_pred = clf.predict(X_train)
    y_valid_pred = clf.predict(X_valid)
    y_test_pred = clf.predict(X_test)  # モデルの予測したカテゴリ
    scores = []
    scores.append(accuracy_score(y_train, y_train_pred))
    scores.append(accuracy_score(y_valid, y_valid_pred))
    scores.append(accuracy_score(y_test, y_test_pred))
    return scores


C = np.logspace(-5, 4, 10, base=10)  # 10^-5~10^4まで均等に１０個の値をリスト形式で生成
solver = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
class_weight = [None, 'balanced']
best_parameter = None
best_scores = None
max_valid_score = 0
scores = []
for c, s, w in itertools.product(C, solver, class_weight):
    print(c, s, w)
    # scores->[train_score,valid_score,test_score]のリスト
    scores = calc_scores(c, s, w)
    print(scores)
    if scores[1] > max_valid_score:  # validデータの正解率が高ければbest_scoreを更新
        max_valid_score = scores[1]
        best_parameter = [c, s, w]
        best_scores = scores

print('best parameter:', best_parameter)
print('best scores: ', best_scores)
print('test accuracy: ', best_scores[2])
