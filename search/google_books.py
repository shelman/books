import json
import requests


class Book:
    def __init__(self, json_resp):
        self.title = json_resp["volumeInfo"]["title"]
        self.main_author = json_resp["volumeInfo"]["authors"][0]
        self.smallThumbnail = json_resp["volumeInfo"]["imageLinks"]["smallThumbnail"]


def dedupe(books):
    seen = set()
    filtered = []
    for book in books:
        if (book.main_author, book.title) not in seen:
            filtered.append(book)
            seen.add((book.main_author, book.title))
    return filtered


def search_books(query):
    r = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")
    response_content = json.loads(r.content)
    return dedupe([Book(json_resp) for json_resp in response_content["items"]])


if __name__ == "__main__":
    import os

    search_books(os.argv[1])
