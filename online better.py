from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
import pickle
import os

#!/home/MisinformedOwl/Env
#%%
def processText(data):
    rows = []
    row = data.lower()

    row = row.replace("#", "")

    rows.append(row)
    #print(row)
    return rows

def preprocess(Data, vec):
    # Tokenize data
    dataRows = processText(Data)
    token = vec.transform(dataRows)

    #exportVectorize(vec)
    return token

def Detect(phrase):
    THIS_FOLDER = os.path.dirname(os.path.abspath("vec.pickle"))
    my_file = os.path.join(THIS_FOLDER, 'vec.pickle')
    inVec = open(my_file, "rb")
    vec = pickle.load(inVec)
    inVec.close()
    THIS_FOLDER = os.path.dirname(os.path.abspath("model.pickle"))
    my_file = os.path.join(THIS_FOLDER, 'model.pickle')
    intree = open(my_file, "rb")
    model = pickle.load(intree)
    intree.close()
    data = preprocess(phrase, vec)
    prob = model.predict_proba(data)
    prob = int(prob[0][1]*100)
    if prob >= 80:
        return 1, prob
    else:
        return 0, prob

app = Flask(__name__, template_folder="template")

app.config['SECRET_KEY'] = '0420d375ca31431af919a03434485509'

#%%
class RegistrationForm(FlaskForm):
    tweetField = TextAreaField('tweet', validators=[DataRequired()])
    submitTweet = SubmitField('Submit')

class returnForm(FlaskForm):
    ret = SubmitField('Return')

@app.route('/', methods=["POST", "GET"])
def index():
    form = RegistrationForm()
    return render_template('index.html', title='Index',form=form)

@app.route('/Detected.html', methods=["POST", "GET"])
def detected():
    if request.method=="POST":
        tweet = request.form['tweet']
    print(tweet)
    form = returnForm()
    res, prob = Detect(tweet)
    if res == 1:
        title = "Depressed"
    else:
        title = "Not Depressed"
    return render_template('Detected.html', title=title, value=[res, prob], form=form)

if __name__ == "__main__":
    app.run(debug=True)