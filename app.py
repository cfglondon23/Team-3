from flask import Flask, render_template, redirect, request, url_for
import json
import air_pollution
app = Flask(__name__, static_url_path='/static')
# app.config['']

'''
city worker
community member
different views 

kensington
canary wharf

---
font: font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
---

• focus on london 
• people can have their own ID (tag London)
• mix of text and images
• scrollable??
• notifications (change or progress)
'''

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form)
        if request.form['password'] == 'cityworker':
            return redirect(url_for('workerfeed'))
        elif request.form['password'] == 'communitymember':
            return redirect(url_for('memberfeed'))
        else:
            return "Invalid credentials"
    return render_template('login.html', error = error)

@app.route('/workerfeed', methods=['GET', 'POST'])
def workerfeed():
    error = None
    if request.method == 'POST':
        return redirect(url_for('city', cityname = request.form['query']))
    return render_template('workerfeed2.html', error = error)

@app.route('/memberfeed', methods=['GET', 'POST'])
def memberfeed():
    return 


# dic = {
#     "london" : [{
#         "link" : "https://i.ytimg.com/vi/OX_6biwM-PY/maxresdefault.jpg",
#         "caption" : "recycling",
#         "account" : "John Doe"}]
# , "bali" : [{
#         "link" : "https://media.istockphoto.com/id/653953140/photo/hindu-temple-in-bali.jpg?s=612x612&w=0&k=20&c=ysj3S2kV1ZgCr4QZWDzjvHRowCI3-cR1xQNnqE8-BS4=",
#         "caption" : "garden",
#         "account" : "Dong"}]
# }

@app.route('/city/<string:cityname>')
def city(cityname):
    citydata = air_pollution.parsed_data['list'][0]['main']['aqi']
    # data = dic[cityname] if cityname in dic else []
    error = None
    # return render_template('city.html', name = cityname, pictures = data, error = error)
    return render_template('index.html', error = error, citydata = citydata)

if __name__ == "__main__":
    app.run(debug=True)