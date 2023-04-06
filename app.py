from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

'''
city worker
community member
different views 

---
font: font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
---

• focus on london 
• people can have their own ID (tag London)
• mix of text and images
• scrollable??
• notifications (change or progress)
'''

@app.route('/x', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == 'cityworker':
            return redirect(url_for('workerfeed'))
        elif request.form['password'] == 'communitymember':
            return redirect(url_for('memberfeed'))
        else:
            return "Invalid credentials"
    return render_template('login.html', error=error)

@app.route('/', methods = ['GET', 'POST'])
def fakelogin():
    error = None
    if request.method == 'POST':
        print(request.form)
        if request.form['password'] == 'cityworker':
            return redirect(url_for('workerfeed'))
        elif request.form['password'] == 'communitymember':
            return redirect(url_for('memberfeed'))
        else:
            return "Invalid credentials"
    return render_template('fakelogin.html', error=error)

@app.route('/workerfeed', methods=['GET', 'POST'])
def workerfeed():
    error = None
    if request.method == 'POST':
        return redirect(url_for('city', cityname = request.form['query']))
    return render_template('workerfeed.html', error=error)

@app.route('/memberfeed', methods=['GET', 'POST'])
def memberfeed():
    return 

@app.route('/city/<string:cityname>')
def city(cityname):
    error = None
    return render_template('city.html', name = cityname, error=error)


if __name__ == "__main__":
    app.run(debug=True)