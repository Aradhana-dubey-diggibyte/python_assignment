import pytest
from srs.util import namedtuple

def test_case_1():
    n = 5
    columns = ['ID', 'MARKS', 'NAME', 'CLASS']
    data = [
        ['1', '97', 'Raymond', '7'],
        ['2', '50', 'Steven', '4'],
        ['3', '91', 'Adrian', '9'],
        ['4', '72', 'Stewart', '5'],
        ['5', '80', 'Peter', '6']
    ]
    assert average_marks(n, columns, data) == 78.00

def test_case_2():
    n = 5
    columns = ['MARKS', 'CLASS', 'NAME', 'ID']
    data = [
        ['92', '2', 'Calum', '1'],
        ['82', '5', 'Scott', '2'],
        ['94', '2', 'Jason', '3'],
        ['55', '8', 'Glenn', '4'],
        ['82', '2', 'Fergus', '5']
    ]
    assert average_marks(n, columns, data) == 81.00
