"""Module for all factories related to this service."""

import os
from importlib import import_module

from flask import Flask
# from flask_demo.extension import celery, redis


dirpath = os.path.dirname(os.path.realpath(__file__))
DEFAULT_CONFIG = os.path.abspath(os.path.join(dirpath, '../../config'))


def create_app(config_file=DEFAULT_CONFIG, *args, **kwargs):
    """Initializes and returns a Flask application given a config."""
    # Right now we don't need to worry about setting up
    #   - blueprints
    #   - templates
    #   - static
    app = Flask(__name__)
    # Set up config
    app.config.from_object('flask_demo.config.DefaultConfig')
    if config_file:
        app.config.from_pyfile(config_file, silent=True)

    # Set up Flak-SqlAlchemy
    db = import_module('flask_demo.models.db').db
    db.init_app(app)

    # # Import DB models. Flask-SQLAlchemy doesn't do this
    # # automatically like Celery does.
    # with app.app_context():
    #     for module in app.config.get('DB_MODELS_IMPORTS', list()):
    #         import_module(module)

    # # Initialize extensions/add-ons/plugins
    # redis.init_app(app)
    # celery.init_app(app)

    return app
