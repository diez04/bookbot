def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    return file_contents

def number_of_words(words):

    words_lst = words.split()
    count = 0

    for word in words_lst:
        count += 1

    return count

def count_characters(text):
    lowercase_text = text.lower()
    count = 0
    character_count = {}

    for char in lowercase_text:
        character_count[char] = lowercase_text.count(char)       
        

    return character_count


def report(word_count, character_count):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char in character_count:
        if char.isalpha():
            print(f"The '{char}' character was found {character_count[char]} times")

    print("--- End report ---")

book = main()
word_number = number_of_words(book)
character_num = count_characters(book)
report(word_number, character_num)
