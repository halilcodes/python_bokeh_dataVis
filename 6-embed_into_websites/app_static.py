# flask app

from flask import Flask, render_template
from datetime import datetime
from basic_line import js, div, cdn_js

# instantiate the flask app
app = Flask(__name__)


# create index page function
@app.route("/")
def index():
    return render_template("index.html",
                           js=js, div=div, cdn_js=cdn_js)


# run the app
if __name__ == "__main__":
    app.run(debug=True)
