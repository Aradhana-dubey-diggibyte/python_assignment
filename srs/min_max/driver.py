
from util import max_of_min

def main():
    X, Y = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(X)]
    result = max_of_min(X, Y, arr)
    print(result)

if __name__ == "__main__":
    main()
