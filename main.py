""" Bookbot """

from stats import *
import sys

print(sys.argv)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
    
        file_contents = f.read()
        return file_contents



def main():
    num_words, word_list = count_words(get_book_text(sys.argv[1]))
    word_dict = count_char(word_list)
    sorted_list_dict = sort_dict(word_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")

    for i in range(0, len(sorted_list_dict)):
        if sorted_list_dict[i]["char"].isalpha():
            print(f"{sorted_list_dict[i]["char"]}: {sorted_list_dict[i]["num"]}")


    print("============= END ===============")

    

main()