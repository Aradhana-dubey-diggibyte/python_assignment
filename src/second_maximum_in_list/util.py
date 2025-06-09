def find_runner_up_score(scores):
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)
    return unique_scores[1] if len(unique_scores) > 1 else None
