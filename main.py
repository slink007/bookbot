def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    word_list = text.split()
    return len(word_list)


def main():
    num_words = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()

