def get_num_words(text):
	words = text.split()
	return len(words)

def get_each_char(text):
	char_count = {}
	for char in text:
		char = char.lower()
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def char_dict_to_list(char_count):
	sorted_list = []
	for char, count in char_count.items():
		sorted_list.append({"char": char, "num": count})
	return sorted_list

def sort_on(sorted_list):
	sorted_dict = sorted([item for item in sorted_list if item["char"].isalpha()], key=lambda x: x["num"], reverse=True)
	return sorted_dict




	