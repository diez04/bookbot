def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    return file_contents

def number_of_words(words):

    words_lst = words.split()
    count = 0

    for word in words_lst:
        count += 1

    print(count)

book = main()
number_of_words(book)
