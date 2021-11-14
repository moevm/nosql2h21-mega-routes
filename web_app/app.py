import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request
from web_app.api import api_bp

from web_app.extensions import csrf_protect


def create_app(config_object="web_app.settings"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    configure_logger(app)
    return app


def register_extensions(app):
    csrf_protect.init_app(app)


def register_blueprints(app):
    app.register_blueprint(api_bp)


def register_errorhandlers(app):

    def render_error(error):
        error_code = getattr(error, "code", 500)
        if error_code == 401:
            app.logger.error(f"Access to '{request.path}' denied. You are not authorized")
        elif error_code == 404:
            app.logger.error(f"Page not found: '{request.path}'")
        elif error_code == 500:
            app.logger.error("Internal server error")
        else:
            app.logger.exception("Unknown error")
        return render_template(f"{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)


def configure_logger(app):
    stream_handler = logging.StreamHandler(sys.stdout)
    Path("logs").mkdir(exist_ok=True)
    log_filename = "logs/flask_logs.log"
    file_handler = RotatingFileHandler(log_filename, maxBytes=10240)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(filename)s: %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    if app.config.get("DEBUG"):
        app.logger.setLevel(logging.DEBUG)
    if not app.logger.handlers:
        app.logger.addHandler(stream_handler)

