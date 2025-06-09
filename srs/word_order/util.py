

def count_words(words):
    word_count = {}
    order = []
    for w in words:
        if w not in word_count:
            order.append(w)
            word_count[w] = 1
        else:
            word_count[w] += 1
    counts = [word_count[w] for w in order]
    return len(order), counts
