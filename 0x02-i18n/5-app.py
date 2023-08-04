#!/usr/bin/env python3
""" Mock logging in """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user(login_as):
    """ Get user from mock db """
    if login_as:
        login_as = int(login_as)
        return users.get(login_as)
    return None


@app.before_request
def before_request():
    """ Before request """
    g.user = get_user(request.args.get('login_as'))


@app.route('/')
def index():
    """ Main index page """
    g.locale = get_locale()
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    logged_in_as = gettext("logged_in_as")
    not_logged_in = gettext("not_logged_in")
    return render_template('5-index.html', home_title=home_title,
                           home_header=home_header, get_locale=get_locale,
                           get_user=g.user, logged_in_as=logged_in_as,
                           not_logged_in=not_logged_in)


# if __name__ == "__main__":
#     app.run(debug=True)
