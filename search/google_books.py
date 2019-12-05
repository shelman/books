import json
import requests


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


def search_books(query):
    r = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")
    response_content = json.loads(r.content)
    return dedupe(response_content["items"])


if __name__ == "__main__":
    search_books()
