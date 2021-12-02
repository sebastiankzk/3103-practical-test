from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import bleach


app = Flask(__name__, template_folder='template')

searches = {}
special_characters = """"!@#$%^&*()-+?_=,<>/"""


@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/home")
def login():
    return render_template('home.html')

@app.route("/search",  methods=['POST'])
def search():
    # ensure POST
    if request.method == 'POST':
        # get input
        input = request.form.get('Search')
        if any(c in special_characters for c in input):
            return render_template('home.html')
        else:
            # sanitise input, eliminating XSS attacks
            # input = bleach.clean(input)
            searches[search] = input
            return render_template('search.html', i=input)

if __name__== "__main__": 
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
