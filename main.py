import sys
from stats import get_num_words
from stats import get_num_lethers
from stats import get_report

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
    

def main():    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    lether_counter = get_num_lethers(book_text)

    print(f"Found {get_num_words(book_text)} total words")
    for element in get_report(lether_counter):
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["count"]}")
        

main()