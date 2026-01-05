import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import joblib

df = pd.read_csv('phishing.csv')

RELIABLE_FEATURES = [
    'UsingIP', 'LongURL', 'ShortURL', 'Symbol@', 
    'Redirecting//', 'PrefixSuffix-', 'SubDomains', 'HTTPS'
]

X = df[RELIABLE_FEATURES]
y = df['class']

model = GradientBoostingClassifier(n_estimators=100, random_state=0)
model.fit(X, y)

joblib.dump(model, 'phishing_model_final.joblib')