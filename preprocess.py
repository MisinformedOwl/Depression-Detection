import pickle

def loadModVec():
    #Extract vectorizer and model
    inVec = open("vec.pickle","rb")
    vec = pickle.load(inVec)
    inVec.close()
    intree = open("model.pickle", "rb")
    model = pickle.load(intree)
    intree.close()
    return vec, model


#%% Used in processing singular strings for use in things like the GUI and the online platform

def processText(data):
    rows = []
    row = data.lower()
    
    row = row.replace("#", "")
    
    #Remove @s
    for r in row.split():
        if r[0] == "@":
            row = row.replace(r+" ", "")
    
    rows.append(row)
    return rows

#A hub for preprocessing the data being used.
def preprocess(Data, vec):
    # Tokenize data
    dataRow = processText(Data)
    token = vec.fit_transform(dataRow)
    
    return token

#%% Preprocess the text data for use in training the model

def processTextData(data):
    rows = []
    for index, row in data.iterrows():
        #Normalise the data so that all text is set to lower case.
        row = row[0].lower()
        
        #Remove all #'s i searched on as to not cause over dependency in the model.
        row = row.replace("#happy", "")
        row = row.replace("#joyful", "")
        row = row.replace("#depressed", "")
        row = row.replace("#sad", "")
        #Remove all hashtags, useless data and normalises the data.
        
        #Remove @s
        for r in row.split():
            if r[0] == "@":
                row = row.replace(r+" ", "")
            
            
        row = row.replace('#', '')
        
        rows.append(row)
    return rows, data['Depressed']

#A hub for preprocessing the data being used.
def preprocessData(Data, vec):
    # Tokenize data
    dataRows, labels = processTextData(Data)
    tokens = vec.fit_transform(dataRows)
    
    return tokens, labels

#%%
def nltkpreprocess(Data):
    # Tokenize data
    featuress = []
    for index, row in Data.iterrows():
        row['Phrases'] = row['Phrases'].replace("\n", "")
        row['Phrases'] = row['Phrases'].replace("#happy", "")
        row['Phrases'] = row['Phrases'].replace("#depressed", "")
        row['Phrases'] = row['Phrases'].replace("#sad", "")
        row['Phrases'] = row['Phrases'].replace("#joyful", "")
        row['Phrases'] = row['Phrases'].replace("#", "")
        tokens = tokenize.word_tokenize(row['Phrases'].lower().strip())
        label = row['Depressed']
        features = {}
        featurelist = ()
        for token in tokens:
            if token not in string.punctuation:
                token.replace("\n", "")
                token.replace("#", "")
                token.replace("happy", "")
                token.replace("depressed", "")
                token.replace("sad", "")
                token.replace("joyful", "")
                if token not in features.keys():
                    features.update({token : 1})
                else:
                    features.update({token : (features.get(token)+1)})
                    
        if label == 1:
            featuress.append((features, 1))
        else:
            featuress.append((features, 0))
    
    featurelist = featuress
    return featurelist

##############################################################################

def nltktestprocess(sentence):
    tokens = tokenize.word_tokenize(sentence.lower().strip())
    features = {}
    for token in tokens:
        if token not in string.punctuation:
            if token not in features.keys():
                features.update({token : 1})
            features.update({token : (features.get(token)+1)})
    return features