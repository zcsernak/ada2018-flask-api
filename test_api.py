import requests

if __name__ == "__main__":
    p = {"p": "40 4"}
    response = requests.get("http://localhost:5000/api/v1.0/random", params=p)
    print(response.text)
