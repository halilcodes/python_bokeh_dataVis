# flask app

from flask import Flask, render_template
from random_generator import js, div, cdn_js

# instantiate the flask app
app = Flask(__name__)


# create index page function
@app.route("/")
def index():
    return render_template("index_dynamic.html",
                           js=js, div=div, cdn_js=cdn_js)


"""this version is not working but neither does the instructor's version
I'll circle back to if when or if I need using it"""

# run the app
if __name__ == "__main__":
    app.run(debug=True)
