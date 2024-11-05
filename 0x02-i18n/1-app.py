#!/usr/bin/env python3
""" 1-app simple flask app with babel """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Config class """
    LANGUAGES = ['en', 'fr']        # The application supported language.
    BABEL_DEFAULT_LOCALE = 'en'     # The default language of the application.
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # The default timezone for the application.


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """ 1-app simple flask app """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
