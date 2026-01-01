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

def sort_key(item):
    return item["num"]

def get_sorted_list(chars_dict):
    sort_list = []
    for character in chars_dict:
            new_dict = {}
            new_dict['char'] = character
            new_dict['num'] = chars_dict[character]
            sort_list.append(new_dict)
    sort_list.sort(reverse=True, key=sort_key)
    return sort_list