
from util import calculate_happiness

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = calculate_happiness(arr, A, B)
    print(result)

if __name__ == "__main__":
    main()
