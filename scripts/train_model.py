from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

queries = [...]  # labeled SQL
labels = [...]   # 0/1

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(queries)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "models/retail_classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")