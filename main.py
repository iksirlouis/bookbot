import sys

from stats import get_num_words, get_char_counts, get_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    numwords = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_list = get_sorted_list(char_counts)
    print_report(book_path,numwords,sorted_list)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path,numwords,sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + str(book_path))
    print("----------- Word Count ----------")
    print("Found " +  str(numwords) + " total words")
    print("--------- Character Count -------")
    
    for item in sorted_list:
        char = item["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {item['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    # This condition ensures the main function runs only when the script 
    # is executed directly and not when imported as a module.
    main()