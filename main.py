from collections import Counter
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    get_report(book_path, word_count, character_count)

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = Counter(text.lower())
    return character_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_report(book_path, words, characters):
    special_characters = [
        " ",
        "'",
        ",",
        "(",
        ")",
        "\n",
        ".",
        "-",
        ":",
        "1",
        "7",
        "2",
        "0",
        "8",
        "[",
        "]",
        "*",
        "?",
        ";",
        "!",
        '"',
        "3",
        "4",
        "5",
        "9",
        "6",
        "_",
        "/",
        "@",
        "$",
        "%",
        "#"
    ]
    sorted_characters = dict(characters.most_common())
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document \n")
    for character in sorted_characters:
        if character not in special_characters:
            print(f"The '{character}' was found {sorted_characters[character]} times")
    print("--- End report ---")
    
main()