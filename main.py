def count_words(file):
    count = 0

    splited_file = file.split()

    for word in splited_file:
        count += 1

    return count

def count_char(file):

    char_count = {}

    file = file.lower()

    for char in file:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count


def main():

    books_path = "books/"
    frankenstein_book = "frankenstein.txt"

    frankenstein_book_path = books_path + frankenstein_book

    with open(frankenstein_book_path) as f:
        file_contents = f.read()

        frankenstein_word_counts = count_words(file_contents)

        print(frankenstein_word_counts)

        print(count_char(file_contents))

        

        
  

main()
