# utils.py
import string
import re
import joblib
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# --- Initialize stopwords and lemmatizer ---
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# --- 1️⃣ Text cleaning function ---
def clean_text_fn(text):
    """
    Input: raw text string
    Output: cleaned text string (lowercase, punctuation removed,
            stopwords removed, lemmatized)
    """
    text = text.lower()  # lowercase
    text = ''.join([c for c in text if c not in string.punctuation])  # remove punctuation
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]  # remove stopwords & lemmatize
    return ' '.join(words)


# --- 2️⃣ Load vectorizer and models once ---
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
models = {
    'Naive Bayes': joblib.load("models/Naive_Bayes.pkl"),
    'Logistic Regression': joblib.load("models/Logistic_Regression.pkl"),
    'Random Forest': joblib.load("models/Random_Forest.pkl")
}


# --- 3️⃣ Prediction function ---
def predict_email(email_text):
    """
    Input: raw email string
    Output: dict of predictions and confidence for each model
    """
    # Clean the email
    email_clean = clean_text_fn(email_text)

    # Convert to TF-IDF
    email_tfidf = vectorizer.transform([email_clean])

    # Run predictions
    results = {}
    for name, model in models.items():
        pred = model.predict(email_tfidf)[0]
        try:
            confidence = model.predict_proba(email_tfidf).max() * 100
            results[name] = (pred, confidence)
        except AttributeError:
            results[name] = (pred, None)

    return results


# --- 4️⃣ Optional: interactive console predictor ---
def interactive_predict():
    """
    Allows user to continuously input emails for prediction in console.
    """
    choice = 1
    while choice == 1:
        email_text = input("Enter the email text:\n> ")
        predictions = predict_email(email_text)
        print("\n=== Model Predictions ===")
        for model_name, (pred, confidence) in predictions.items():
            if confidence is not None:
                print(f"{model_name}: {pred} ({confidence:.2f}% confident)")
            else:
                print(f"{model_name}: {pred}")
        print("\n✅ Prediction complete.\n")
        choice = int(input("Enter 1 to predict another email, 0 to exit: "))
