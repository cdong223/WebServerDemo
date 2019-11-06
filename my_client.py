import requests

def make_a_request():
    r = requests.get("http://127.0.0.1:5000/info")
    print(r)
    print(r.text)
    answer = r.json()
    print(answer["Author"])


def call_sum():
    x = {"a": 10, "b": -2}
    r = requests.post("http://127.0.0.1:5000/sum", json=x)
    answer = r.json()
    print(answer)


if __name__ == "__main__":
    make_a_request()
    call_sum()
