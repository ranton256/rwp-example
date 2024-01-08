import urllib3

from typing import Optional


def download_url(url: str, file_path: Optional[str] = None) -> bool:
    resp = urllib3.request("GET", url)
    if resp.status == 200:
        if file_path is None:
            print(resp.data)
        else:
            with open(file_path, "wb") as f:
                f.write(resp.data)
    return resp.status == 200
