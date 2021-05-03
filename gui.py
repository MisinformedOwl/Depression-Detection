#Import tkinter and pickle for both making the gui and importing the model
import tkinter as tk
import pickle

#%%
#Create tkinter window and give it a name
window = tk.Tk()
window.title("Depression classification GUI")

#%%
#Preprocess the text exactly like in Naive.py
def processText(data):
    rows = []
    row = data.lower()
    
    row = row.replace("#happy", "")
    row = row.replace("#joyful", "")
    row = row.replace("#depressed", "")
    row = row.replace("#sad", "")
    row = row.replace("#", "")
    
    rows.append(row)
    return rows

#%%
#Preprocess exactly like in Naive.py
def preprocess(Data, vec):
    # Tokenize data
    dataRows = processText(Data)
    token = vec.transform(dataRows)
    
    #exportVectorize(vec)
    return token

#%%
#The function for calling preprocessing and predicting depression then sending to the gui.
def Detect(vec, model):
    #Get the data in the text box and preprocess
    data = preprocess(text_box.get("1.0", "end"), vec)
    #Calculate the probability as a %
    prob = model.predict_proba(data)
    #Get the absolute prediction (0 or 1)
    res = int(model.predict(data))
    #Make probability between 0% and 100%
    prob = int(prob[0][1]*100)
    #If depressed...
    if res == 1:
        #Remove the text in the text box and replace with the probability
        results.config(text = f"Depressed {prob}%")
    else: #If not depressed...
        results.config(text = f"Not Depressed {prob}%")

#Acquire the vectorizer and model using pickle
inVec = open("vec.pickle","rb")
vec = pickle.load(inVec)
inVec.close()
insvc = open("model.pickle", "rb")
model = pickle.load(insvc)
insvc.close()

#Create the text box and the submit button
text_box = tk.Text()
text_box.grid(column=0,row=0,columnspan=2)

submit = tk.Button(text = "Classify", command=lambda:Detect(vec, model))
submit.grid(column=0,row=1)

results=tk.Label(text = "Not Depressed 0%")
results.grid(column=1,row=1)

window.mainloop()