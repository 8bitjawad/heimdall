# 📧 Heimdall - Intelligent Email Classifier

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://heimdall.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> **Automatically categorize your emails into 6 distinct categories with 98%+ accuracy using machine learning**

🔗 **[Try it Live!](https://heimdall.streamlit.app/)** | 📊 [View Project](#) | 📝 [Documentation](#how-to-run-locally)

---

## 🎯 Problem Statement

In today's digital world, users receive **hundreds of emails daily** — from promotions, social media notifications, forums, verification codes, to general updates. 

**The Challenge:**
- ⏰ Manually sorting through emails is **time-consuming**
- 🚨 Misclassified emails (especially spam or verification codes) can have **serious consequences**
- 📬 Important emails get lost in the clutter

**Our Solution:** An automated email classification system powered by machine learning.

---

## ✨ Features

- 🤖 **Three ML Models** - Compare predictions from Naive Bayes, Logistic Regression, and Random Forest
- 🎯 **High Accuracy** - Achieves 97-98% classification accuracy
- 📊 **Confidence Scoring** - See how confident each model is about its prediction
- 🚀 **Real-time Classification** - Instant results via interactive web interface
- 🧹 **Automatic Text Preprocessing** - Handles cleaning, tokenization, and feature extraction
- 🌐 **Cloud Deployed** - Access anywhere via Streamlit Cloud

---

## 📂 Email Categories

The system classifies emails into **6 distinct categories:**

| Category | Description | Example |
|----------|-------------|---------|
| 🎁 **Promotions** | Marketing emails, sales, offers | "50% OFF - Limited Time Sale!" |
| 🚫 **Spam** | Unwanted/suspicious emails | "You've won $1,000,000!" |
| 📱 **Social Media** | Notifications from social platforms | "John liked your post" |
| 💬 **Forum** | Discussion boards, community updates | "New reply to your thread" |
| 🔐 **Verification Code** | OTP, 2FA codes, account verification | "Your code is 482917" |
| 📰 **Updates** | General newsletters, product updates | "Weekly digest from Medium" |

---

## 🛠️ Solution Architecture

```
Input Email Text
       ↓
Text Preprocessing Pipeline
  • Lowercasing
  • Punctuation Removal
  • Stopwords Removal  
  • Lemmatization
       ↓
TF-IDF Vectorization
       ↓
Three ML Models (Parallel Prediction)
  • Naive Bayes
  • Logistic Regression
  • Random Forest
       ↓
Category + Confidence Score
```

---

## 📊 Model Performance

Evaluated on **2,696 test emails** across 6 categories:

| Model | Accuracy | Precision | Recall | F1-Score | Key Strength |
|-------|----------|-----------|--------|----------|--------------|
| **Logistic Regression** ⭐ | **98.48%** | 98.49% | 98.48% | 98.48% | Best overall performer |
| Random Forest | 98.18% | 98.20% | 98.18% | 98.18% | Robust predictions |
| Naive Bayes | 97.92% | 97.94% | 97.92% | 97.92% | Fastest inference |

### 🎯 Category-wise Performance

All models achieve **97-100% precision** across categories:
- ✅ **Verification Code**: 99-100% (most reliable)
- ✅ **Promotions**: 98-100% (highly accurate)
- ✅ **Spam**: 98-99% (excellent detection)
- ✅ **Social Media**: 98-99% (consistent)
- ✅ **Forum**: 96-98% (strong performance)
- ⚠️ **Updates**: 96-97% (slightly challenging due to varied content)

---

## 💻 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-154f3c?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

- **Machine Learning**: scikit-learn (Naive Bayes, Logistic Regression, Random Forest)
- **NLP Processing**: NLTK (stopwords, lemmatization)
- **Feature Engineering**: TF-IDF Vectorization
- **Model Persistence**: Joblib
- **Web Framework**: Streamlit
- **Data Handling**: Pandas, NumPy
- **Deployment**: Streamlit Cloud

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
pip or conda package manager
```

### Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/email-classifier.git
cd email-classifier
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Download NLTK data** (first time only)
```python
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"
```

4️⃣ **Run the app**
```bash
streamlit run app.py
```

5️⃣ **Open your browser** and navigate to `http://localhost:8501`

---

## 🎮 How to Use

### Web Interface

1. **Enter Email Text** - Paste any email content into the text area
2. **Click Classify** - Models automatically preprocess and predict
3. **View Results** - See predictions from all three models with confidence scores

### Example Usage

**Input:**
```
Your verification code is 482917. 
Please use this code within 10 minutes.
```

**Output:**
```
=== Model Predictions ===

Naive Bayes: 
  Category: verify_code 
  Confidence: 99.2% ✅

Logistic Regression: 
  Category: verify_code 
  Confidence: 99.0% ✅

Random Forest: 
  Category: verify_code 
  Confidence: 86.0% ✅
```

---

## 📁 Project Structure

```
email-classifier/
├── app.py                      # Streamlit web application
├── utils.py                    # Preprocessing & prediction functions
├── requirements.txt            # Python dependencies
├── models/
│   ├── naive_bayes_model.pkl   # Trained Naive Bayes model
│   ├── logistic_model.pkl      # Trained Logistic Regression
│   ├── random_forest_model.pkl # Trained Random Forest
│   └── tfidf_vectorizer.pkl    # Fitted TF-IDF vectorizer
├── notebooks/
│   └── training.ipynb          # Model training & evaluation
└── README.md                   # Project documentation
```

---

## 🔬 Methodology

### 1. Data Preprocessing Pipeline

```python
def preprocess_text(text):
    # Lowercase conversion
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenization & stopword removal
    tokens = [word for word in text.split() if word not in stopwords]
    
    # Lemmatization
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    
    return ' '.join(lemmatized)
```

### 2. Feature Extraction

- **TF-IDF Vectorization** converts preprocessed text into numerical features
- Captures word importance across the entire corpus
- Reduces dimensionality while preserving semantic meaning

### 3. Model Selection Rationale

**Why Logistic Regression?**
- ⚡ **Best accuracy** (98.48%) among all models
- 🚀 **Fast inference** - suitable for real-time applications
- 📊 **Balanced precision-recall** across all categories
- 💾 **Low memory footprint** - ideal for deployment

---

## 📈 Future Enhancements

- [ ] 📦 **Batch Processing** - Upload CSV files with multiple emails
- [ ] 📊 **Advanced Visualizations** - Interactive charts for predictions
- [ ] 🔄 **Active Learning** - User feedback loop to improve accuracy
- [ ] 🌍 **Multi-language Support** - Classify emails in different languages
- [ ] 📧 **Email API Integration** - Direct Gmail/Outlook integration
- [ ] 🧠 **Deep Learning Models** - Experiment with BERT/Transformers
- [ ] 📱 **Mobile App** - Native iOS/Android application

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**

- 🌐 Portfolio: [yourwebsite.com](#)
- 💼 LinkedIn: [linkedin.com/in/yourprofile](#)
- 🐙 GitHub: [@yourusername](#)

---

## 🙏 Acknowledgments

- Dataset source: [Link to dataset](#)
- Built with [Streamlit](https://streamlit.io/)
- ML models powered by [scikit-learn](https://scikit-learn.org/)

---

<div align="center">

### ⭐ Star this repo if you found it helpful!

**[Live Demo](https://heimdall.streamlit.app/)** • **[Report Bug](#)** • **[Request Feature](#)**

Made with ❤️ and ☕

</div>
