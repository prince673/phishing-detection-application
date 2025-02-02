import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Example dataset (replace with your dataset)
data = {
    "url_length": [50, 30, 70, 20],
    "num_dots": [2, 1, 3, 1],
    "num_hyphens": [1, 0, 2, 0],
    "num_at": [0, 0, 1, 0],
    "num_question": [1, 0, 2, 0],
    "num_equal": [1, 0, 2, 0],
    "label": [1, 0, 1, 0]  # 1 = phishing, 0 = legitimate
}

df = pd.DataFrame(data)

# Feature extraction
X = df.drop("label", axis=1)
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")