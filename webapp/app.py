import os

from flask import Flask, render_template, request

from search.google_books import search_books


def dedupe(results):
    seen = set()
    filtered = []
    for result in results:
        if (
            result["volumeInfo"]["authors"][0],
            result["volumeInfo"]["title"],
        ) not in seen:
            filtered.append(result)
            seen.add(
                (result["volumeInfo"]["authors"][0], result["volumeInfo"]["title"])
            )
    return filtered


def attach_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/search")
    def search():
        results = search_books(request.args.get("query"))
        results = dedupe(results)
        return render_template("search.html", results=results)


def create_app():
    app_directory = os.path.dirname(os.path.realpath(__file__))
    template_folder = os.path.join(app_directory, "templates")

    app = Flask("books", template_folder=template_folder)
    attach_routes(app)
    app.debug = True
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
