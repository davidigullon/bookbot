from stats import get_word_count, num_characters


def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	filepath = "./books/frankenstein.txt"
	book_text = get_book_text(filepath)
	word_count = get_word_count(book_text)
	characters = num_characters(book_text)
	print(f"{word_count} words found in the document")
	print(characters)

if __name__ == '__main__':
	main()
