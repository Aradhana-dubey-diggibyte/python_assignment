
from util import can_stack_cubes

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        print(can_stack_cubes(cubes))

if __name__ == "__main__":
    main()
