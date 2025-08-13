def get_word_count(text):
    return len(text.split())

def get_symbols_count_ignore_case(text):
    text = text.lower()

    stats = {}
    for letter in text:
        if letter not in stats:
            stats[letter] = 1
        else:
            stats[letter] += 1

    return stats

def sort_on(items):
    return items[1]

def get_sorted_list_stats(stats):
    return sorted(stats.items(), key = sort_on, reverse=True)
