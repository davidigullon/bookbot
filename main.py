import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book = sys.argv[1]

from stats import get_num_words
from stats import get_each_char
from stats import char_dict_to_list
from stats import sort_on

def get_book_text(path):
	with open(path) as f:
		return f.read()


def main():
	path = book
	text = get_book_text(path)
	num_words = get_num_words(text)
	char_count = get_each_char(text)
	sorted_list = char_dict_to_list(char_count)
	sorted_dict = sort_on(sorted_list)
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_dict:
		print(f"{item["char"]}: {item["num"]}")

main()
