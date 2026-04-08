import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Sample minimal dataset (just to make app run)
data = {
    'runs_left': [100, 50, 30, 60],
    'balls_left': [60, 30, 20, 40],
    'wickets': [5, 3, 2, 4],
    'total_runs_x': [180, 150, 140, 170],
    'crr': [6.5, 7.0, 8.0, 6.8],
    'rrr': [8.0, 9.0, 10.0, 7.5]
}

df = pd.DataFrame(data)
X = df
y = [0, 1, 1, 0]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, 'pipe.pkl')

print("✅ pipe.pkl created")