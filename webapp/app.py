import os

from flask import Flask, render_template, request

from search.google_books import search_books


class App(Flask):

    def __init__(self, name, folder, *args, **kwargs):
        template_folder = os.path.join(folder, "pages")
        super().__init__(name, template_folder=template_folder, *args, **kwargs)
        self.folder = folder

    def attach_index(self):
        @self.route("/")
        def index():
            return render_template("index.html")

    def attach_search(self):
        @self.route("/search")
        def search():
            results = search_books(request.args.get("query"))
            return render_template("search/search.html", results=results)

    def configure(self):
        self.debug = True


if __name__ == "__main__":
    app = App("books", os.path.dirname(os.path.realpath(__file__)))
    app.configure()
    app.attach_index()
    app.attach_search()
    app.run()
