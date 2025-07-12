
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


def make_dict_list(char_dict):
	dict_list = []
	for key in char_dict.keys():
		dict_list.append( {"char": key, "num": char_dict[key]} )
	dict_list.sort(reverse=True, key=lambda x: x["num"])
	return dict_list
	

	
