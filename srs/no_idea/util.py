

def calculate_happiness(arr, A, B):
    happiness = 0
    set_A = set(A)
    set_B = set(B)
    for num in arr:
        if num in set_A:
            happiness += 1
        elif num in set_B:
            happiness -= 1
    return happiness
