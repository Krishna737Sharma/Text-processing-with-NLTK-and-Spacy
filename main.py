#Importing useful libraries
import nltk
import spacy
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt')
import zipfile
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns

# Load SpaCy language model for English
nlp = spacy.load("en_core_web_sm")

# Load and unzip the dataset
with zipfile.ZipFile('/content/sms+spam+collection.zip', 'r') as zip_ref:
    zip_ref.extractall('sms_spam_data')

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
data = []
with open('/content/sms_spam_data/SMSSpamCollection', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            tag, message = line.split('\t')
            data.append([tag, message])

df= pd.DataFrame(data, columns=['target', 'text'])

display(df)

"""# **Data Preprocessing**"""

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df['target'] = encoder.fit_transform(df['target'])

df.head()

df.isnull().sum()

df.duplicated().sum()

df=df.drop_duplicates(keep='first')

df.duplicated().sum()

df.shape

df.head()

df['target'].value_counts()

import matplotlib.pyplot as plt
plt.figure(figsize=(6,3))
plt.pie(df['target'].value_counts(), labels=['ham', 'spam'], autopct='%1.1f%%')
plt.show()

# number of character
df['num_characters'] = df['text'].apply(len)
df.head()

#number of words
df['num_words'] = df['text'].apply(lambda x:len(nltk.word_tokenize(x)))
df.head()

#number of sentences
df['num_sentences'] = df['text'].apply(lambda x:len(nltk.sent_tokenize(x)))
df.head()

# count of digits in sentence
df['num_digits'] = df['text'].apply(lambda x:sum([1 if w.isdigit() else 0 for w in x.split()]))
df.head()

# number of special character in sentence
df['num_special_char'] = df['text'].apply(lambda x:sum([1 if w.isalnum() else 0 for w in x.split()]))
df.head()

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def nltk_process_text(text):
    # Tokenization
    tokens = word_tokenize(text)

    # Stopwords Removal
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in tokens if word.lower() not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    # Join the processed words back into a string
    transformed_text = ' '.join(lemmatized_words)

    return transformed_text

# Apply the NLTK processing function to the 'text' column
df['transformed_text'] = df['text'].apply(nltk_process_text)

df.head()

from wordcloud import WordCloud
wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')

spam_wc=wc.generate(df[df['target']==1]['transformed_text'].str.cat(sep=" "))

plt.figure(figsize=(15,6))
plt.imshow(spam_wc)

ham_wc=wc.generate(df[df['target']==0]['transformed_text'].str.cat(sep=" "))

plt.figure(figsize=(15,6))
plt.imshow(ham_wc)

spam_corpus=[]
for msg in df[df['target']==1]['transformed_text'].tolist():
    for word in msg.split():
        spam_corpus.append(word)

len(spam_corpus)

from collections import Counter
plt.figure(figsize=(15,6))
top_30_words = Counter(spam_corpus).most_common(30)
sns.barplot(x=[x[0] for x in top_30_words], y=[x[1] for x in top_30_words])
plt.xticks(rotation='vertical')
plt.show()

ham_corpus=[]
for msg in df[df['target']==0]['transformed_text'].tolist():
    for word in msg.split():
        ham_corpus.append(word)

plt.figure(figsize=(15,6))
top_30_words = Counter(ham_corpus).most_common(30)
sns.barplot(x=[x[0] for x in top_30_words], y=[x[1] for x in top_30_words])
plt.xticks(rotation='vertical')
plt.show()

# SpaCy Processing: Named Entity Recognition (NER)
doc = nlp(' '.join(df['transformed_text']) )
entities = [(ent.text, ent.label_) for ent in doc.ents]

from spacy import displacy

# Render the named entities visually
displacy.render(doc, style="ent", jupyter=True)

import spacy
import pandas as pd

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

# Process the text data
docs = df['transformed_text'].apply(nlp)

# Define functions to extract NER and POS information
def extract_ner(doc):
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def extract_pos(doc):
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags

# Apply the functions to the processed documents
df['ner'] = docs.apply(extract_ner)
df['pos_tags'] = docs.apply(extract_pos)

# Create categorical columns for NER and POS
ner_labels = set([label for entities in df['ner'] for text, label in entities])
pos_tags_labels = set([label for tags in df['pos_tags'] for text, label in tags])

df['ner_category'] = df['ner'].apply(lambda x: [label for text, label in x])
df['pos_tag_category'] = df['pos_tags'].apply(lambda x: [label for text, label in x])

# Create numerical columns for NER and POS
df['ner_count'] = df['ner'].apply(len)
df['pos_tag_count'] = df['pos_tags'].apply(len)

df.head()

df.dtypes

# Select categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Drop categorical columns
data = df.drop(categorical_cols, axis=1)

print(data.head())



"""# **IG calculation**"""

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import mutual_info_classif

# Separate the features and target variable
x = data.drop(columns=['target'], axis=1)
y = data['target']

# standardaize the dataset
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x = scaler.fit_transform(x)

print(x)

# Calculate the information gain for each feature
# this function use same formula that mensioned into the question

ig = mutual_info_classif(x, y)

ig

# Assume the target variable is the first column
target = data.columns[0]
features = data.columns[1:]

# Create a dictionary to store the feature and its information gain
ig_dict = {}
for feature, ig_value in zip(features, ig):
    ig_dict[feature] = ig_value

ig_dict

# Sort the dictionary by the information gain in descending order
ig_dict_sorted = dict(sorted(ig_dict.items(), key=lambda item: item[1], reverse=True))

# Select the top n features with the highest information gain
n = 3
selected_features = list(ig_dict_sorted.keys())[:n]

# Print the selected features
print('Selected Features:')
print(selected_features)

# Visualize the information gain of each feature
sns.set(style="whitegrid")
sns.set(rc={'figure.figsize':(4,2)})
sns.barplot(x=list(ig_dict_sorted.values()), y=list(ig_dict_sorted.keys()))
plt.title('Information Gain of Features')
plt.xlabel('Information Gain')
plt.ylabel('Feature Name')
plt.show()

#creating new dataset according to selected_features

dfnew = df[['target','text','transformed_text'] + selected_features]

dfnew.head()

"""# **Data Exploration**"""

dfnew.loc[:, dfnew.columns != 'target'].describe()

# targeting ham
dfnew[dfnew['target']==0].describe()

# targeting spam
dfnew[dfnew['target']==1].describe()

import seaborn as sns
plt.figure(figsize=(12,6))
sns.histplot(dfnew[dfnew['target']==0]['num_characters'])
sns.histplot(dfnew[dfnew['target']==1]['num_characters'],color='red')

plt.figure(figsize=(12,6))
sns.histplot(dfnew[dfnew['target']==0]['ner_count'])
sns.histplot(dfnew[dfnew['target']==1]['ner_count'],color='red')

plt.figure(figsize=(12,6))
sns.histplot(dfnew[dfnew['target']==0]['num_digits'])
sns.histplot(dfnew[dfnew['target']==1]['num_digits'],color='red')

sns.pairplot(dfnew,hue='target')

import seaborn as sns
import matplotlib.pyplot as plt

# Select only numerical features for correlation calculation
numerical_df = df.select_dtypes(include=['number'])

# Calculate the correlation matrix for numerical features
corr_matrix = numerical_df.corr()

# Plot the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(corr_matrix, annot=True)
plt.show()

"""# **Model**"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, classification_report

cv=CountVectorizer()
tfidf=TfidfVectorizer(max_features=3000)

X=tfidf.fit_transform(dfnew['transformed_text']).toarray()
y=dfnew['target'].values

X.shape

y.shape

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

gnb=GaussianNB()
mnb=MultinomialNB()
bnb=BernoulliNB()

gnb.fit(X_train,y_train)
y_pred1=gnb.predict(X_test)
print(accuracy_score(y_test,y_pred1))
print(classification_report(y_test,y_pred1))

mnb.fit(X_train,y_train)
y_pred2=mnb.predict(X_test)
print(accuracy_score(y_test,y_pred2))
print(classification_report(y_test,y_pred2))

bnb.fit(X_train,y_train)
y_pred3=bnb.predict(X_test)
print(accuracy_score(y_test,y_pred3))
print(classification_report(y_test,y_pred3))

svc=SVC(kernel='sigmoid',gamma=1.0)
knc=KNeighborsClassifier()
mnb=MultinomialNB()
dtc=DecisionTreeClassifier(max_depth=5)
lrc=LogisticRegression(solver='liblinear',penalty='l1')
rfn=RandomForestClassifier()
abc=AdaBoostClassifier()
bc=BaggingClassifier()
etc=ExtraTreesClassifier()
gbdt=GradientBoostingClassifier()
xgb=XGBClassifier()

clf={
    'SVC':svc,
    'KN':knc,
    'NB':mnb,
    'DT':dtc,
    'LR':lrc,
    'RF':rfn,
    'AdaBoost':abc,
    'BgC':bc,
    'ETC':etc,
    'GBDT':gbdt,
    'xgb':xgb
}

def train_clf(clf,X_train,y_train,X_test,y_test):
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    precision=precision_score(y_test,y_pred)

    return accuracy,precision

from sklearn.metrics import accuracy_score, precision_score

accuracy_scores = []
precision_scores = []

for name, clf1 in clf.items():
    current_accuracy, current_precision = train_clf(clf1, X_train, y_train, X_test, y_test)

    print(f'{name} accuracy is {current_accuracy}')
    print(f'{name} precision is {current_precision}\n\n')

    accuracy_scores.append(current_accuracy)
    precision_scores.append(current_precision)

# plot of classifiers with accuracy and precision score
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,8))  # Use figsize instead of passing width and height separately
plt.bar(clf.keys(), accuracy_scores, color='blue', label='Accuracy')
plt.bar(clf.keys(), precision_scores, color='red', alpha=0.7, label='Precision')  # Add alpha for transparency
plt.xlabel('Classifiers')
plt.ylabel('Scores')
plt.title('Classifier Accuracy and Precision Scores')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()  # Display legend
plt.tight_layout()  # Ensure labels fit within plot area
plt.show()

