#!/usr/bin/env python3
""" Get locale from request """
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Babel Config Class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 2-index.html
    """
    g.locale = get_locale()
    return render_template("2-index.html", get_locale=get_locale)
