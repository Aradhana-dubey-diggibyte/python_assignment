
from util import filter_valid_emails

def main():
    n = int(input())
    emails = [input().strip() for _ in range(n)]
    valid_emails = filter_valid_emails(emails)
    print(valid_emails)

if __name__ == "__main__":
    main()
