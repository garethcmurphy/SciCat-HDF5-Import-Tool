#!/usr/bin/env python3
"""post to scicat"""


class SciCatPost:
    """post to scicat"""

    url_base = "https://scicatapi.esss.dk"

    def __init__(self):
        self.url_base = "http://localhost:3000"

    def post(self):
        """post to scicat"""
        print(self.url_base)


if __name__ == "__main__":
    SCI = SciCatPost()
    SCI.post()
