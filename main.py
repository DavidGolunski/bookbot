from stats import *
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main(): 
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)

    word_count = get_num_words(book_text)
    # print(f"{word_count} words found in the document")

    char_counts = get_char_counts(book_text)
    # print(char_counts)

    sorted_char_list = get_sorted_char_list(char_counts)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for index in range(len(sorted_char_list)):
        char_dict = sorted_char_list[index]
        if not char_dict["char"].isalpha():
            continue
        print(f"{char_dict['char']}: {char_dict['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()