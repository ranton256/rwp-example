from typing import Optional

import urllib3
from bs4 import BeautifulSoup


def download_url(url: str, file_path: Optional[str] = None) -> bool:
    resp = urllib3.request("GET", url)
    good: bool = False
    if resp.status == 200:
        soup = BeautifulSoup(resp.data, "html.parser")
        output = soup.prettify()
        if file_path is None:
            print(output)
        else:
            with open(file_path, "w") as f:
                f.write(output)
        good = True
    return good
