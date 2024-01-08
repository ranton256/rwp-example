#!/usr/bin/python
import argparse

import urllib3


def main(url, file_path=None):
    print(f"Downloading {url}")
    resp = urllib3.request("GET", my_url)
    print(f"Response status was {resp.status}")
    if resp.status == 200:
        if file_path is None:
            print(resp.data)
        else:
            print(f"Saving to {file_path}")
            with open(file_path, "wb") as f:
                f.write(resp.data)
    return resp.status == 200


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="url to download")
    parser.add_argument(
        "-f",
        "--file_path",
        help="file path to save URL contents to, if not set writes to stdout",
    )
    args = parser.parse_args()

    if args.url:
        my_url = args.url
    else:
        my_url = "https://en.wikipedia.org/wiki/Monty_Python"

    main(my_url, args.file_path)
