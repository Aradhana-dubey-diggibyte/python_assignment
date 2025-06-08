from srs.iterators.util import calculate_probability

def test_sample_input_1():
    assert calculate_probability(4, ['a', 'a', 'c', 'd'], 2) == 0.8333

def test_sample_input_2():
    assert calculate_probability(5, ['a', 'b', 'c', 'a', 'd'], 3) == 0.9
