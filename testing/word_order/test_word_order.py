
from srs.word_order.util import count_words

def test_count_words():
    words = ["bcdef", "abcdefg", "bcde", "bcdef"]
    distinct, counts = count_words(words)
    assert distinct == 3
    assert counts == [2, 1, 1]

    words2 = ["apple", "banana", "apple", "orange", "banana", "banana"]
    distinct2, counts2 = count_words(words2)
    assert distinct2 == 3
    assert counts2 == [2, 3, 1]
