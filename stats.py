def get_word_count(text):
	words = text.split()
	return len(words)

def num_characters(text):
	characters = {}
	for char in text.lower():
		if char in characters:
			characters[char] += 1
		else:
			characters[char] = 1
	return characters

def sort_on(item):
	return item["num"]

def sort_character_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
	char_list = [{"char": ch, "num": count} for ch, count in char_counts.items() if ch.isalpha()]
	char_list.sort(reverse=True, key=sort_on)
	return char_list

