# opening the book .txt
# path needs to be relative or absolute to where the main.py file is locates
# ls on terminal returns the list of folders

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text_from_file(book_path)
    words_list = count_words_text(book_text)
    total_letters_count = letter_count(book_text) # returns a dict
    sorted_list_characters = get_list_dict(total_letters_count)
    # print (f'{book_name} has {words_list} words in it')
    # print (total_letters_count)
    print ("||","==="*5, "Book Report", "==="*5, "||")
    print ()
    print (f'This book has {words_list} words in it')
    print ()
    print ("And below is how many times each character appeared, in ascending order")
    print ("="*49)
    create_book_report(sorted_list_characters)
    print ("="*49)
    print ()
    print ("||","="*13, "Report finished", "="*13,"||")


def get_text_from_file(path_file): # this function reads the .txt as a string
    with open(path_file) as f:
        return f.read()

def count_words_text(book_text): # this function returns the size of the string (# of words in the string)
    book_list_words = book_text.split()
    return len(book_list_words)

def list_sort(dict_word_count): # function to be used as a parameter to a .sort() method on a list
    return dict_word_count['quantity']

def letter_count(words_list):
    normalized_letter = words_list.lower() # this returns each character of the string lowercased for the assignment, since we are counting the letter itself, regardless of the casing
    letter_dict = {}
    for letter in normalized_letter:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def get_list_dict(letter_dict):
    sorted_list_dict = []
    # this function generates a list with nested dictionaries
    # and sorts it ascending
    for letter, quantity in letter_dict.items():
        temp_dict = {"character" : letter, "quantity" : quantity}
        sorted_list_dict.append(temp_dict)
    sorted_list_dict.sort(reverse=True, key=list_sort)
    return sorted_list_dict

def create_book_report(dict):
    for i in dict:
        if i['character'].isalpha(): # check to print ONLY letters
            print (f' The character {i['character']} was found {i['quantity']} times')
    return None


main()