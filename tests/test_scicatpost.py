"""test"""
from scicat_post import SciCatPost


def test_scicat():
    """test"""
    sci = SciCatPost()
    assert isinstance(sci.url_base, str)
