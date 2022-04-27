import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier

df = pd.read_csv('german_credit_data.csv')
df.fillna('NaN', inplace=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)


x = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

model = CatBoostClassifier(iterations=2,
                           learning_rate=1,
                           depth=2)
model.fit(X_train, y_train, ['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose'] )

pickle.dump(model, open('german_credit.pkl', 'wb'))
