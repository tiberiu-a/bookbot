def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    # nr_words = number_of_words(text)
    # print(f"{nr_words} words found in the document.")
    list_words = list_of_words(text)
    char_count = count_characters(list_words)
    list_dict = list_of_dict(char_count)
    list_dict.sort(reverse=True, key=sort_on)
    print_raport(list_dict, list_words, path)
    

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def number_of_words(string):
    list_of_words = list_of_words()
    nr_words = len(list_of_words)
    return nr_words

def list_of_words(string):
    return string.split()

def count_characters(words_list):
    char_count = {}
    for word in words_list:
        word = word.lower()
        for char in word:            
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def list_of_dict(char_count):
    list_dict = []
    for key in char_count:
        list_dict.append({"char": key, "num": char_count[key]})
    return list_dict

def sort_on(dict):
    return dict["num"]

def print_raport(list, list_words, text_path):
    print(f"--- Begin raport of {text_path} ---")
    word_count = len(list_words)
    print(f"{word_count} words found in the document")
    for dict in list:
        print(f"The '{dict['char']}' character was found {dict['num']} times")
    print("--- End report ---")

main()
