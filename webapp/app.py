from flask import Flask


def attach_routes(app):
    @app.route("/")
    def index():
        return "Hello"


def create_app():
    app = Flask("books")
    attach_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
