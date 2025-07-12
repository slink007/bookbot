
def count_words(text):
    word_list = text.split()
    return len(word_list)


def count_characters(text):
    letter_dictionary = {}
    for t in text:
        t = t.lower()
        if t in letter_dictionary:
            letter_dictionary[t] = letter_dictionary[t] + 1
        else:
            letter_dictionary[t] = 1
    return letter_dictionary
