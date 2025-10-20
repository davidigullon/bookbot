def get_word_count(text):
    words = text.split()
    return len(words)

def num_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_characters):
    sorted_list = []
    for ch in num_characters:
        sorted_list.append({"char": ch, "num": num_characters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list