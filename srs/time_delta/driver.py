from util import time_difference

def main():
    t = int(input().strip())
    for _ in range(t):
        t1 = input().strip()
        t2 = input().strip()
        print(time_difference(t1, t2))

if __name__ == "__main__":
    main()
