#!/usr/bin/env python3
""" Force locale with URL parameter"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Babel config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Get locale from request """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """ Main index page """
    g.locale = get_locale()
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template('4-index.html', home_title=home_title,
                           home_header=home_header, get_locale=get_locale)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")
