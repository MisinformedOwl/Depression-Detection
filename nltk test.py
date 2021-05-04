from nltk import tokenize, ngrams, NaiveBayesClassifier
import nltk
from nltk.corpus import stopwords
import pandas as pd
import string
import random
import pickle
import preprocess

def export(model):
    with open("model.pickle", "wb") as out:
        pickle.dump(model, out)

#%%
def matrix(confusion):
    tn,fp,fn,tp = confusion.flatten()
    print(f"True negative: {tn}")
    print(f"False negative: {fn}")
    print(f"True positive: {tp}")
    print(f"False positive: {fp}")

#%%

fileData = pd.read_excel("data/data.xlsx")
training = []
testing = []
stopwords = set(stopwords.words('english'))

size = len(fileData)
size = round((size/100)*80)

fileData = fileData.sample(frac=1)
trainingText = fileData[:size]
testingText = fileData[size:]

print("training")
print(trainingText)
print("testing")
print(testingText)

training = preprocess.nltkpreprocess(trainingText)
testing = preprocess.nltkpreprocess(testingText)

nb = NaiveBayesClassifier.train(training)
    
print()
print(f"Naive bayes accuracy: %{(nltk.classify.accuracy(nb, testing))*100}")
print(nb.most_informative_features(5))

print()

export(nb)
