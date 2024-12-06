# SMS Spam Classifier with NLTK and SpaCy

This project aims to build a classifier to detect whether an SMS message is 'spam' or 'ham' (legitimate). The dataset provided contains around 5000 SMS messages along with their corresponding labels ('spam' or 'ham').

The task involves loading the dataset, splitting it into training and testing datasets, performing feature selection based on Information Gain (IG), and using the selected features to build a classifier. The analysis results will show the effectiveness of the selected features and the accuracy scores for both training and testing splits.

## Objectives

- **Data Preprocessing**: Load the dataset and split it into training and testing datasets.
- **Feature Selection**: Use Information Gain (IG) as the criterion to select important features that help classify SMS messages as 'spam' or 'ham'.
- **Build Classifier**: Train a classifier using the selected features and evaluate its performance.
- **Analysis**: Show the accuracy of the classifier on both the training and testing splits.

## Steps

### 1. Dataset Overview

The 'sms_spam_dataset.zip' file contains:
- A set of SMS messages.
- Labels for each SMS indicating whether it is 'spam' or 'ham' (legitimate).

### 2. Data Preprocessing

- **Load the Dataset**: Unzip the dataset and load it into a suitable data structure.
- **Split the Data**: Split the dataset into a training set (used for model building and feature selection) and a testing set (used for evaluating model performance).

### 3. Feature Extraction

- **Text Preprocessing**: 
  - Tokenize the messages using SpaCy and NLTK.
  - Remove stop words, punctuation, and other irrelevant features.
  - Lemmatize the words to reduce them to their base forms.

- **Information Gain (IG) Feature Selection**:
  - Compute the entropy of the entire dataset.
  - Calculate the entropy for subsets based on each feature.
  - Select the top features that contribute most to reducing uncertainty (i.e., Information Gain).

### 4. Model Building

- **Train Classifier**: Use machine learning models such as Naive Bayes or SVM to build the classifier based on the selected features.
- **Evaluate Performance**: Evaluate the classifier on both the training and testing datasets.
  - Show accuracy scores for both splits.
  - Plot confusion matrices or classification reports to provide additional insights.

### 5. Results and Analysis

- Show the feature selection process.
- Display accuracy scores for training and testing sets.
- Discuss the effectiveness of the selected features and their impact on classifier performance.

### Key Libraries

- **NLTK**: For text preprocessing tasks like tokenization, removing stop words, and lemmatization.
- **SpaCy**: For advanced NLP features, such as tokenization, part-of-speech tagging, and lemmatization.
- **scikit-learn**: For machine learning models like Naive Bayes, SVM, and performance evaluation metrics.

### Prerequisites

Ensure you have the following libraries installed:

```bash
pip install nltk spacy scikit-learn pandas numpy
