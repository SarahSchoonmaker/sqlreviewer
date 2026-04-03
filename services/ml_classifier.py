import joblib

model = joblib.load("models/retail_classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_retail(sql: str):
    X = vectorizer.transform([sql])
    prob = model.predict_proba(X)[0][1]
    pred = prob > 0.5

    return pred, float(prob)