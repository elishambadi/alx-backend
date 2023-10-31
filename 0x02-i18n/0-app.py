#!/usr/bin/env python3
"""Flask Babel Module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Home Page for App"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
