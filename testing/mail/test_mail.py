from srs.mail.util import is_valid_email, filter_valid_emails

def test_is_valid_email():
    assert is_valid_email("lara@hackerrank.com")
    assert is_valid_email("brian-23@hackerrank.com")
    assert is_valid_email("britts_54@hackerrank.com")
    assert not is_valid_email("john@doe.corporate")  # extension > 3
    assert not is_valid_email("invalid@.com")
    assert not is_valid_email("missingatsign.com")

def test_filter_valid_emails():
    emails = [
        "lara@hackerrank.com",
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com",
        "invalid@.com"
    ]
    expected = [
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com",
        "lara@hackerrank.com"
    ]
    assert filter_valid_emails(emails) == expected
