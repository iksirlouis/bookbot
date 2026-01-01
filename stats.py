def get_num_words(text):
    word_count = len(text.split())
    return word_count

def get_char_counts(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] = character_count[char] + 1
        else:
            character_count[char] = 1
    return character_count

def get_sorted_list(dict)
    