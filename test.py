import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import seaborn as sns
from nltk.corpus import stopwords

sns.set(color_codes=True)


#//////////////////////////////////numerical data/////////////////////////////////////////////////
data = pd.read_csv("camera_dataset.csv")
data.drop(labels='Model', axis=1, inplace=True)
data.dropna(axis=0,inplace=True)
#//////////////////////////////////text_mining/////////////////////////////////////////////////
# with open("../../../../Users/Abdul-Rahman.R/Desktop/txt_mining.txt") as data2:
#     contents = data2.read()
#     print(contents)

 
#//////////////////////////summmary////////////////////////////////////////////////
data.describe(include='all')
#///////////////////////////describe attributes////////////////////////////////////
data.info()
#///////////////////////////find relations between the variables///////////////////
plt.Figure(figsize=(20,10))
d=data.corr()
sns.heatmap(d,cmap="BrBG",annot=True)
print(d)
plt.show()


#                        //text_mining///
with open("txt_mining.txt") as data2:
    content = data2.read()
    print(content)


#[Lowering]
input_str=content.lower()
print(input_str)


#[Remove puntuation]
import string

result = content.translate(str.maketrans('','', string.punctuation))
print(result)


#word_tokenize
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize

tokens = word_tokenize(content)
result = [i for i in tokens if not i in stop_words] #  for loop inside array 
print (result)


#[Stremming] return the verb to its source
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

input_str = word_tokenize(content)
for word in input_str:
  print(stemmer.stem(word))


print("___________________________________________")
#[Lemmatization]
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer=WordNetLemmatizer()

input_str=word_tokenize(content)
for word in input_str:
  print(lemmatizer.lemmatize(word))

nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer

with open("../../../../Users/User/Desktop/Python/txt_mining.txt") as f:
    contents = f.readlines()
for sentence in contents:
    s = SentimentIntensityAnalyzer()
    vs=s.polarity_scores(sentence)
    print(sentence, str(vs))





     

