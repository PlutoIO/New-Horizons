import base64
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def encode_token(username: str, token: str) -> str:
    print(token)
    t = base64.b64encode(f"{username}:{token}".encode("ascii")).decode("ascii")
    return t


def get_user_data(username: str) -> requests.Response.content:
    _url = "https://api.github.com/user"
    _encoded_token = encode_token(username, os.getenv("GIT_PERSONAL_ACCESS_TOKEN"))
    _headers = {"Authorization": f"Basic {_encoded_token}"}
    return requests.post(url=_url, headers=_headers).text

#
# with open("log.json", "w+") as file:
#     file.write(get_user_data("PlutoIO"))
#     file.close()
