import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
     return render_template("index.html", page_title="Portfolio for Horseshoedev")

if __name__ == '__main__':
    app.debug = False
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')))