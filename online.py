from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pickle

import preprocess

def Detect(phrase):
    vec, model = preprocess.loadModVec()
    #Preprcess and predict.
    data = preprocess.preprocess(phrase, vec)
    prob = model.predict_proba(data)
    res = int(model.predict(data))
    prob = int(prob[0][1]*100)
    if res == 1:
        return 1
    else:
        return 0

#Create flask app
app = Flask(__name__, template_folder="template")
#Add the secret key. (Required for forms)
app.config['SECRET_KEY'] = '0420d375ca31431af919a03434485509'

#%%
#Contains the materials for the form
class DetectionForm(FlaskForm):
    tweetField = StringField('tweet', validators=[DataRequired()])
    submitTweet = SubmitField('Submit')

#The form used to return
class returnForm(FlaskForm):
    ret = SubmitField('Return')

#The main and only page, loads the text box and submit button for classification
@app.route('/', methods=["POST", "GET"])
def index():
    form = DetectionForm()
    return render_template('index.html', title='Index',form=form)

#updates the page to inform the user of the result. And leaves a button to return the text box. for anotehr classification
@app.route('/Detected.html', methods=["POST", "GET"])
def detected():
    #If the method used is post return the tweet data.
    if request.method=="POST":
        tweet = request.form['tweet']
    print(tweet)
    form = returnForm()
    res = Detect(tweet)
    if res == 1:
        title = "Depressed"
    else:
        title = "Not Depressed"
    return render_template('Detected.html', title=title, value=res, form=form)
    

#Main function for running the server
if __name__ == "__main__":
    app.run(debug=True)