def count_words(file):
    count = 0

    splited_file = file.split()

    for word in splited_file:
        count += 1

    return count

def count_char(file):

    char_count = {}

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    file = file.lower()

    for char in file:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for c in alphabet:
        print(f"The '{c}' character was found {char_count[c]} times")


def main():

    books_path = "books/"
    frankenstein_book = "frankenstein.txt"

    frankenstein_book_path = books_path + frankenstein_book

    with open(frankenstein_book_path) as f:
        file_contents = f.read()

        frankenstein_word_counts = count_words(file_contents)

        print(f"--- Begin report of {frankenstein_book_path} ---")

        print(f"{frankenstein_word_counts} words found in the document")
        print("\n")
        print("\n")

        count_char(file_contents)

        print("--- End report ---")

main()
