
from util import determinant

def main():
    n = int(input())
    matrix = [list(map(float, input().split())) for _ in range(n)]
    print(determinant(matrix))

if __name__ == "__main__":
    main()
