from flask import Flask
import logging
from decouple import config

from infx_semantic_normalization_api.management import (
    management_views as management_views,
)
from infx_semantic_normalization_api.mapping import mapping_views as mapping_views


log_level = config("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)


def create_app():
    """
    Initializes and returns the Flask app instance.
    Sets up configurations and registers routes and error handlers.
    """
    app = Flask(__name__)
    app.register_blueprint(management_views.management_blueprint)
    app.register_blueprint(mapping_views.mapping_blueprint)

    @app.get("/ping")
    def ping():
        logger.info("Pinged!")
        return "pong", 200

    return app


application = create_app()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5500)
