from flask import Flask


from . import __version__


def create_app():
    """
    Create a Flask applicatio using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__)

    @app.route("/")
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return "Hello World"

    return app


def main():
    app = create_app()
    app.run()
