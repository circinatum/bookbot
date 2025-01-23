def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)

    print(f"\n--- Begin report of {book_path} ---\n")
    print(f"{num_words} words found in the document\n")
    
    char_count_sorted = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
    char_count = dict(char_count_sorted)
    for key, value in char_count.items():
        print(f"The '{key}' character was found {value} times")
    
    print("--- End report ---")  

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for char in text:
        char_lowered = char.lower()
        if char_lowered.isalpha():
            if char_lowered in char_dict:
                old = char_dict[char_lowered]
                new = old + 1
                char_dict[char_lowered] = new
            else:
                char_dict[char_lowered] = 1
    return char_dict


main()