import json
import requests


def search():
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=nickel+boys")
    response_content = json.loads(r.content)
    pass

if __name__ == "__main__":
    search()
