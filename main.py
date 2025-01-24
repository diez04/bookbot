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

def count_characters(text):
    lowercase_text = text.lower()
    count = 0
    character_count = {}

    for char in lowercase_text:
        character_count[char] = lowercase_text.count(char)       
        

    return character_count


book = main()
print(count_characters(book))
