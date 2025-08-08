def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	filepath = "./books/frankenstein.txt"
	book_text = get_book_text(filepath)
	print(book_text)

if __name__ == '__main__':
	main()
