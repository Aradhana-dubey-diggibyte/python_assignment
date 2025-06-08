import pytest
from srs.mutations.util import mutate_string

def test_mutate_string():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"
    assert mutate_string("hello", 0, "y") == "yello"
    assert mutate_string("hello", 4, "z") == "hellz"
    assert mutate_string("abcdef", 3, "X") == "abcXef"
    assert mutate_string("aaaaa", 2, "b") == "aabaa"
