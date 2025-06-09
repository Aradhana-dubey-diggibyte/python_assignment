
from util import count_words

def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]

    distinct_count, counts = count_words(words)
    print(distinct_count)
    print(' '.join(map(str, counts)))

if __name__ == "__main__":
    main()
