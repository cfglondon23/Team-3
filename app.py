from flask import Flask, render_template, redirect, request, url_for
import json
from flask_sqlalchemy import SQLAlchemy
import data_calculations

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartcity.db'
db = SQLAlchemy(app)

class CityDB(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    connectivity = db.Column(db.Float)
    energy = db.Column(db.Float)
    health_and_safety = db.Column(db.Float)
    materials = db.Column(db.Float)
    mobility = db.Column(db.Float)
    placemaking = db.Column(db.Float)
'''
---
font: font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
---
'''
@app.route('/', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == 'cityworker':
            return redirect(url_for('workerfeed'))
        elif request.form['password'] == 'communitymember':
            return redirect(url_for('memberfeed'))
        else:
            return "Invalid credentials"
    return render_template('login.html', error = error)

@app.route('/traffic')
def traffic():
    return render_template('traffic.html')

@app.route('/waste')
def waste():
    return render_template('waste.html')

@app.route('/workerfeed')
def workerfeed():
    error = None
    return render_template('feed.html', error = error)

@app.route('/notification')
def memberfeed():
    return render_template('notification.html')

@app.route('/leaderboards')
def leaderboards():
    return render_template('leaderboards.html')

@app.route('/user/<username>')
def user(username):
    error = None
    return render_template(username + '.html', error = error)

if __name__ == "__main__":
    app.run(debug=True)