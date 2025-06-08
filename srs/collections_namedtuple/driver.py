def main():
    n = int(input())
    columns = input().split()
    data = [input().split() for _ in range(n)]
    
    from srs.util import average_marks
    avg = average_marks(n, columns, data)
    
    print(f"{avg:.2f}")

if __name__ == "__main__":
    main()
