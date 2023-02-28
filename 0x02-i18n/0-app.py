#!/usr/bin/env python3
"""Flask Application
"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home():
    """Returns home route
       Returns: html template
    """
    return render_template("0-index.html")

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
