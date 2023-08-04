#!/usr/bin/env python3
""" Display the current time """
from datetime import datetime
import pytz.exceptions
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext, format_datetime


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
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Get locale from request """
    # Priority 1 - URL parameter
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    # Priority 2 - User setting
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in Config.LANGUAGES:
            return locale
    # Priority 3 - Accept-Language header
    locale = request.headers.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    # Priority 4 - Default locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    """ Get timezone from request """
    # Priority 1 - URL parameter
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Priority 2 - User setting
    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            try:
                pytz.timezone(timezone)
                return timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    # Priority 3 - Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


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
    """ Index page """
    g.locale = get_locale()
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    logged_in_as = gettext("logged_in_as")
    not_logged_in = gettext("not_logged_in")

    # Get the user's timezone
    user_timezone = pytz.timezone(get_timezone())

    # Get the current UTC time
    current_time = datetime.utcnow()

    # Convert the UTC time to the user's timezone
    localized_time = current_time.astimezone(user_timezone)

    # Format the date in the user's preferred language
    current_time_str = format_datetime(localized_time, format='medium')

    current_time_is = gettext("current_time_is")
    return render_template('index.html', home_title=home_title,
                           home_header=home_header, get_locale=get_locale,
                           get_user=g.user, logged_in_as=logged_in_as,
                           not_logged_in=not_logged_in,
                           current_time=current_time_str,
                           current_time_is=current_time_is)


if __name__ == "__main__":
    app.run(debug=True)
