#%%
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd
import pickle
from sklearn import naive_bayes
from sklearn.metrics import confusion_matrix
import preprocess

#%%
#Export both the vectorizer and model for future use
def export(vec, model):
    with open("vec.pickle", "wb") as out:
        pickle.dump(vec, out)
    
    with open("model.pickle", "wb") as out:
        pickle.dump(model, out)

#%%
#Display a confusion matrix for added debugging since my dataset was not balanced
def matrix(confusion):
    #Confusion is a list flattened into individual variables. for ease of use
    tn,fp,fn,tp = confusion.flatten()
    print(f"True negative: {tn}")
    print(f"False negative: {fn}")
    print(f"True positive: {tp}")
    print(f"False positive: {fp}")


#%%
#Load the data from the excel file
fileData = pd.read_excel("data/data.xlsx")

#Create stopwords
stopwords = set(stopwords.words('english'))

#Create the configure the vectorizer
vec = CountVectorizer(lowercase=True, analyzer='word', ngram_range=(1,3), strip_accents='ascii', max_df=80)

#Create the naive bayes classifier
Classifier = naive_bayes.ComplementNB()
#Classifier = LogisticRegression()
#Get the data and randomize it
fileData = fileData.sample(frac=1)
Text = fileData[:]

#Preprocess data, get data and labels
data, labels = preprocess.preprocessData(Text, vec)

#Test to see if label and data size is the same
print(f"Training size: {data.shape[0]}")
print(f"Labels size: {len(labels)}")

#Split data into training and testing
train_x, test_x, train_y, test_y = train_test_split(data, labels, test_size=0.2, shuffle=True)

#Train the model
nb = Classifier.fit(train_x, train_y)

#Export the vectorizer and the model for use in other programs.
export(vec,nb)

#Display a % prediction for the first 10 labels.
for index in range (1, 10):
    res = nb.predict_proba(test_x[index])
    res = int(res[0][1]*100)
    print(f"{res}%")

#Displayt the accuracy of the model
print(f"Accuracy is: {nb.score(test_x,test_y)*100}%")

#Predict the test set again so it can be used in the confusion matrix.
pred_y = nb.predict(test_x)

confusion = confusion_matrix(test_y, pred_y)

matrix(confusion)