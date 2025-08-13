import sys
from stats import get_word_count
from stats import get_symbols_count_ignore_case
from stats import get_sorted_list_stats

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    text = get_book_text(path)

    print("----------- Word Count ----------")
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    stats = get_symbols_count_ignore_case(text);
    sorted_stats  = get_sorted_list_stats(stats)
    for k, v in sorted_stats:
        print(f"{k}: {v}")

main()
