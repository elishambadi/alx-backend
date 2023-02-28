#!/usr/bin/env python3
"""Config class with Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]

    def get_locale():
        return request.accept_languages.best_match(Config.LANGUAGES)

    def get_timezone():
        return 'UTC'


app = Flask(__name__)
babel = Babel(app,
              locale_selector=Config.get_locale,
              timezone_selector=Config.get_timezone)


@app.route('/')
def home():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
