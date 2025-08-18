from stats import get_word_count, num_characters, sort_character_counts
import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	filepath = sys.argv[1]
	book_text = get_book_text(filepath)
	word_count = get_word_count(book_text)
	characters = num_characters(book_text)
	sorted_count = sort_character_counts(characters)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}.")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for item in sorted_count:
		print(f"{item['char']}: {item["num"]}")
	print("============= END ===============")

if __name__ == '__main__':
	main()
