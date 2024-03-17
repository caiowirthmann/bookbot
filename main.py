# opening the book .txt

# path needs to be relative or absolute to where the main.py file is locates
# ls on terminal returns the list of folders

def main():
    book_path = "books/frankenstein.txt"
    book_text, book_name = get_text_from_file(book_path)
    word_list = count_words_text(book_text)
    print (f'{book_name} has {word_list} words in it')

    with open("books/frankenstein.txt") as file_text:
        file_content = file_text.read()

def get_text_from_file(path_file): # this function reads the .txt as a string and split it
    with open(path_file) as f:
        return f.read(), f.name

def count_words_text(book_text):
    book_list_words = book_text.split()
    return len(book_list_words)


main()