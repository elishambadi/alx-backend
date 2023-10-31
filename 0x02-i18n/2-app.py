#!/usr/bin/env python3
"""Flask Babel Module"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


# Can be stored in a separate file
class Config:
    """Configuration class for Flask"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = app(Babel)


@babel.localeselector
def get_locale():
    """Gets the most suitable locale"""
    return request.accept_languages.best_match(['en', 'es'])


@app.route('/')
def home():
    """Home Page for App"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
