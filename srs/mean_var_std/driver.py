from util import calculate_mean_var_std

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mean_result, var_result, std_result = calculate_mean_var_std(arr)
    
    print(mean_result)
    print(var_result)
    print(std_result)

if __name__ == "__main__":
    main()
