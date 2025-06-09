def merge_the_tools(string, k):
    result = []
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        seen = set()
        merged = ''
        for char in substring:
            if char not in seen:
                seen.add(char)
                merged += char
        result.append(merged)
    return result
