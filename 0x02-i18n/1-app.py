#!/usr/bin/env python3
"""Config class with Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LANGUAGE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def home():
    return render_template("1-index.html")


app.config.from_object(Config)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
