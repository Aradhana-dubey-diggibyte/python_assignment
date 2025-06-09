import io
import sys
from string_formating.util import print_formatted

def test_print_formatted(capsys):
    print_formatted(5)
    captured = capsys.readouterr()
    expected_output = (
        "  1   1   1   1\n"
        "  2   2   2  10\n"
        "  3   3   3  11\n"
        "  4   4   4 100\n"
        "  5   5   5 101\n"
    )
    assert captured.out == expected_output
