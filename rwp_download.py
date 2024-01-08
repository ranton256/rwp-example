#!/usr/bin/python
import urllib3


def main():
    print("Hello,world!")
    my_url = "https://en.wikipedia.org/wiki/Monty_Python"
    resp = urllib3.request("GET", my_url)
    print(f"Response status was {resp.status}")
    if resp.status == 200:
        print(resp.data)


if __name__ == "__main__":
    main()
