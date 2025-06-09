def find_average(marks_dict, query_name):
    scores = marks_dict.get(query_name, [])
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)
