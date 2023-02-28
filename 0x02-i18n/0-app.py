#!/usr/bin/env python3
"""Flask Application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Returns home route
       Returns: html template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
