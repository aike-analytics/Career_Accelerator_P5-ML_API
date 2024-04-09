import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
import pickle
from fastapi import FastAPI, HTTPException
import uvicorn

df = pd.read_csv('Paitients_Files_Train.csv')
df['sepsis_encoded'] = df['Sepssis'].map({'Positive':1, 'Negative': 0})
df = df.drop(['ID', 'Sepssis'], axis='columns')

X_train = df.drop('sepsis_encoded', axis='columns')
y_train = df['sepsis_encoded']

scaler = MinMaxScaler()
scaler_fit = scaler.fit(X_train) 
X_train_scaled = scaler_fit.transform(X_train)


optimizer = RandomizedSearchCV(GradientBoostingClassifier(), {
    'loss': ['deviance', 'exponential'],
    'learning_rate': [0.05, 0.1, 0.5],
    'n_estimators': [50, 100, 150, 200],
    'criterion': ['friedman_mse', 'squared_error'],
    'max_features': ['sqrt', 'log2']
    }, refit=True)

optimizer.fit(X_train_scaled, y_train)
best_params = optimizer.best_params_

final_model = GradientBoostingClassifier(criterion=best_params['criterion'], 
                                         learning_rate=best_params['learning_rate'], loss=best_params['loss'], 
                                         max_features=best_params['max_features'], n_estimators=best_params['n_estimators'])
final_model.fit(X_train_scaled, y_train)


with open("model.pkl", "wb") as file:
    pickle.dump(final_model, file)

with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler_fit, file)


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Sepsis Illness Prediction"}

@app.get("/predict/")
async def predict_sepsis(PRG: int, PL: int, PR: int, SK: int, TS: int, M11: float, BD2: float, Age: int, Insurance: int):
    try:
        with open("model.pkl", "rb") as file:
            model = pickle.load(file)
        with open("scaler.pkl", "rb") as file:
            scaler_fit = pickle.load(file)
        
        X = [[PRG, PL, PR, SK, TS, M11, BD2, Age, Insurance]]
        X_scaled = scaler_fit.transform(X)
        pred = model.predict(X_scaled)
        prediction_prob = model.predict_proba(X_scaled)[0, 1] if pred[0] == 1 else model.predict_proba(X_scaled)[0, 0]
        return {'Prediction': int(pred[0]), 'Probability': f'{round(prediction_prob*100,2)}%'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
