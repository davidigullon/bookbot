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
