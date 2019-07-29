"""test"""
from get_files import GetFiles


def test_answer():
    """test"""
    getter = GetFiles()

    assert getter.suffix == ".hdf5"
