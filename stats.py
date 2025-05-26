def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words



def char_dict(file_contents):
    character_dictionary = {}
    characters = list(file_contents)
    for character in characters:
        lower_char = character.lower()
        if lower_char in character_dictionary:
            character_dictionary[lower_char] += 1
        else:
            character_dictionary[lower_char] = 1
    return character_dictionary


def report(file_contents):
    char_report = [] 
    def sort_on(d):
        return d["num"]
    for char, count in file_contents.items():
        char_report.append({"char": char, "num": count})
    char_report.sort(reverse=True, key=sort_on)
    return char_report

