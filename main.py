def main():
    book_path = "books/frankestein.txt"
    book = get_text(book_path)
    words = count_words(book)
    characters = count_characters(book)
    character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print(f"--Report on the book: {book_path}--")
    print(f"There are {words} words in the book")
    print()
    for character in character_list:
        print(f"The {character} character appears {characters[character]} times.")
    print()
    print("--End of the report --")


def get_text(path):
    with open(path) as f:
        return f.read()
    

def count_words(text):
    word_list = text.split()
    return len(word_list)


def count_characters(text):
    base_text = text.lower()
    character_count = {}
    for character in base_text:
        if not character.isalpha():
            pass
        elif character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count


main()
