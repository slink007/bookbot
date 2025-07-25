import sys
from stats import count_words, count_characters, make_dict_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def print_report(word_count, sorted_list, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for sl in sorted_list:
        if sl['char'].isalpha():
            print(f"{sl['char']}: {sl['num']}")


def usage():
    print(f"Usage: python3 {sys.argv[0]} <path_to_book>")


def main():
    if (len(sys.argv) == 1):
        usage()
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    ccnt = count_characters(text)
    sorted_list = make_dict_list(ccnt)
    print_report(word_count=num_words, sorted_list=sorted_list, path=book_path)


if __name__ == "__main__":
    main()

