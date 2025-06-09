import itertools

def calculate_probability(n, letters, k):
    total_combinations = list(itertools.combinations(range(n), k))
    count_with_a = sum(1 for comb in total_combinations if any(letters[i] == 'a' for i in comb))
    return round(count_with_a / len(total_combinations), 4)
