from stats import  get_num_words
from stats import character_count
import sys

def get_book_text(book_path):
	with open(book_path) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	num_words = get_num_words(book_text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	my_count = character_count(book_text)
	sorted_counts = sorted(my_count.items(), key=lambda item: item[1], reverse=True)
	for char, count in sorted_counts:
		if char.isalpha() == True:	
			print(f"{char}: {count}")
	print("============= END ===============")

if __name__ == "__main__":
    main()

