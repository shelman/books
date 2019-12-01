from flask import Flask, render_template, request

from search.google_books import search_books


def attach_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/search")
    def search():
        results = search_books(request.args.get("query"))
        return render_template("search.html", results=results)


def create_app():
    app = Flask("books")
    attach_routes(app)
    app.debug = True
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
