#!/usr/bin/python
import argparse

from rwp_example.rwp_download_url import download_url


def main(url, file_path=None):
    print(f"Downloading {url}")
    if file_path:
        print(f"Saving to {file_path}")
    return download_url(url, file_path)


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
