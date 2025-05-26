from stats import count_words, char_dict, report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    character_dictionary = char_dict(text)
    print (f"Analyzing book found at {sys.argv[1]}")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    char_report = report(character_dictionary)
    for char in char_report:
        if char["char"].isalpha():
            print(f'{char["char"]}: {char["num"]}')
    print ("============= END ===============")

main()
