from stats import word_count, character_count, sort_character_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    book_contents = get_book_text(path_to_book)
    count = word_count(book_contents)
    letter_count = character_count(book_contents)
    sorted_list = sort_character_count(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for each in sorted_list:
        if each["char"].isalpha():
            print(f"{each['char']}: {each['num']}")
    print("============= END ===============")

main()