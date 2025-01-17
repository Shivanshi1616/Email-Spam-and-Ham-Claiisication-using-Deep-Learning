# Email-Spam-and-Ham-Claiisication-using-Deep-Learning

# 📧🤖 Mail Spam & Ham Classifier

## 📝 Project Overview
This project is designed to classify emails as either **"Ham"** (legitimate) or **"Spam"** (unwanted). The goal is to use advanced machine learning techniques to build an accurate email classifier capable of identifying spam efficiently. The classification labels used are:
- `0`: Ham (Legitimate email)
- `1`: Spam (Unwanted email)

---

## 📂 Dataset Used
- **Dataset Columns:**
  - `mail_message`: Contains the email text content.
  - `label`: Binary labels (`0` for Ham and `1` for Spam) indicating the classification of the message.

---

## 🎯 Objective
The primary objective of this project is to:
1. Build an intelligent system that classifies emails with high accuracy.
2. Assist users in managing their emails by filtering spam.
3. Leverage machine learning and NLP for robust spam detection.

---

## 🛠️ Tools and Techniques Used
### Python Libraries:
- **`pandas`** & **`numpy`**: For data organization and manipulation.
- **`re`**: For efficient text cleaning using regular expressions.
- **`CountVectorizer`** & **`TfidfVectorizer`**: For text feature extraction through Bag of Words (BoW) and TF-IDF techniques.
- **`scikit-learn`**: For model implementation and performance evaluation.
- **`matplotlib`** & **`seaborn`**: For creating visual insights, such as confusion matrices.
- **`pickle`** & **`joblib`**: For saving and reusing trained models.

### Machine Learning Algorithms:
- **`MultinomialNB`**: Handles multinomial data (text frequencies) efficiently.
- **`GaussianNB`**: Suitable for continuous data distributions.
- **`BernoulliNB`**: Used for binary or boolean features.

---

## 🔄 Workflow
### 1. Text Preprocessing
- Emails were cleaned using **Regex (re)**, focusing on removing unnecessary characters, whitespace, and special symbols.
- Converted text into lowercase and tokenized for consistency in processing.

### 2. Feature Extraction
- Extracted features using **Bag of Words (CountVectorizer)** and **TF-IDF Vectorizer**, capturing the importance of words within the dataset.

### 3. Model Training & Evaluation
- Trained classifiers (MultinomialNB, GaussianNB, and BernoulliNB) on the processed data.
- Evaluated models based on metrics such as:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **F1-score**
  - **Confusion Matrix**

### 4. Performance Insights
- Analyzed results using detailed visualizations, classification reports, and confusion matrices.

---

## 🤔 Key Questions Answered
- How accurately can we classify emails into spam or ham?
- Which features contribute most to distinguishing spam from ham?
- How does the system perform across different models and evaluation metrics?

---

## 📚 Learnings from the Project
1. **Natural Language Processing (NLP)**:
   - Text cleaning, tokenization, and feature engineering.
   - Working with text-based datasets for classification.
2. **Naive Bayes Algorithms**:
   - Comparison and analysis of performance metrics for MultinomialNB, GaussianNB, and BernoulliNB.
3. **Data Visualization**:
   - Generated visual reports like confusion matrices for model evaluation.

---

## 🌟 Highlights of the Project
- **Robust Preprocessing**: Emails are thoroughly cleaned and prepped for analysis.
- **Accurate Classifiers**: Naive Bayes algorithms showcase exceptional performance in text classification tasks.
- **Reusable Model**: Saved models can be integrated into email systems for real-time filtering.

---

## 📊 Results Summary
- High accuracy and performance across the implemented models.
- Clear differentiation of features important for spam detection.
- Interactive visualizations provided actionable insights into model performance.
