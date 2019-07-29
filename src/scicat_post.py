#!/usr/bin/env python3
"""post to scicat"""


class SciCatPost:
    """post to scicat"""

    url_base = "http://scicatapi.esss.dk"

    def __init__(self):
        pass

    def post(self):
        """post to scicat"""
        print(self.url_base)


if __name__ == "__main__":
    SCI = SciCatPost()
    SCI.post()
