from util import calculate_probability

if __name__ == "__main__":
    n = int(input())
    letters = input().split()
    k = int(input())
    print(calculate_probability(n, letters, k))
