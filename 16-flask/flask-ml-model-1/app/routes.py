from flask import Flask, render_template, request
import pickle
import numpy as np
from . import app, db

# app = Flask(__name__)

model = pickle.load(open('Forest_Model.pkl', 'rb'))
vectorizer = pickle.load(open('Forest_Model_vectorizer.pkl', 'rb'))


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/review")
def review():
    return render_template('review.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        review = request.form['review']
        test_bag = vectorizer.transform([review]).toarray()
        test_predictions = model.predict(test_bag)
        print('test_predictions[0]', test_predictions[0], int(test_predictions[0]))
        db_query = "INSERT INTO review(review, prediction) VALUES('" + review + "', " + str(test_predictions[0]) + ")" 
        res = db.engine.execute(db_query)
        # print('res', res.fetchall())
        result = 'Positive review' if test_predictions[0] else 'Negative Review'
        return render_template("result.html", value=[review,result])

@app.route('/data')
def data():
    print('inside data route')
    res = db.engine.execute("SELECT * FROM review" ).fetchall()
    return render_template("data.html", values=res)

@app.route('/feedback', methods=['POST'])
def feedback():
    print('fdsfdsfsdaf')
    if request.method == 'POST':
        feedback = request.form['feedback']
        print('feedback', feedback)
        return render_template('home.html')