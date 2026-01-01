from stats import get_num_words, get_char_counts

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    numwords = get_num_words(text)
    print("Found " +  str(numwords) + " total words")
    char_counts = get_char_counts(text)
    print(char_counts)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


if __name__ == "__main__":
    # This condition ensures the main function runs only when the script 
    # is executed directly and not when imported as a module.
    main()