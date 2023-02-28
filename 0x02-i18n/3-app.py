#!/usr/bin/env python3
"""Config class with Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LANGUAGE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


#  Babel
def get_locale():
    """Gets best locale
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


babel.init_app(app, locale_selector=get_locale)
#  End of Babel


#  App routes
@app.route('/')
def home():
    """Renders home page
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
