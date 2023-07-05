import requests

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def get_response(url):
    return requests.get(url)

if __name__ == "__main__":
    res = get_response(api_url)
    print(res)


# TODO TDD (Test Driven Development), Unit Testing