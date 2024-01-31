from flask import Flask


def create_app():
    """
    Initializes and returns the Flask app instance.
    Sets up configurations and registers routes and error handlers.
    """
    app = Flask(__name__)

    @app.get("/ping")
    def ping():
        return "pong", 200

    return app


application = create_app()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)
