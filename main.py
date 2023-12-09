from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap5
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_KEY']
Bootstrap5(app)


@app.route('/')
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)