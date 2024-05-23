import requests
import threading
import time


def make_request(url):
    start = time.time()
    response = requests.get(url)
    time_taken = time.time() - start
    print(f"{response.text}, time: {time_taken}")


def main():
    urls = ["http://127.0.0.1:8000/polls?delay=0"] * 100
    # urls = [
    #     "http://127.0.0.1:8000/polls?delay=3",
    #     "http://127.0.0.1:8000/polls?delay=2",
    #     "http://127.0.0.1:8000/polls?delay=1",
    #     ]

    threads = []
    for url in urls:
        thread = threading.Thread(target=make_request, args=(url,))
        threads.append(thread)
        thread.start()


if __name__ == "__main__":
    main()
