import json
import requests


def search_books(query):
    r = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")
    response_content = json.loads(r.content)
    return response_content["items"]


if __name__ == "__main__":
    search_books()
