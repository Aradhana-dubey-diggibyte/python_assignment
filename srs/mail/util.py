

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email) is not None

def filter_valid_emails(emails):
    return sorted(filter(is_valid_email, emails))
