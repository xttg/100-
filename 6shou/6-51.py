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
np.savetxt('feature/train.feature.txt',
           X_train.toarray(), fmt='%d')  # スパース行列から密行列に変換
np.savetxt('feature/valid.feature.txt', X_valid.toarray(), fmt='%d')
np.savetxt('feature/test.feature.txt', X_test.toarray(), fmt='%d')
