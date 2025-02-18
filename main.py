def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_total = word_count(file_contents)
    char_dict = char_count(file_contents)
    letter_dict = alph_only(file_contents)
    #print report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_total} words found in the document \n")
    for l,c in letter_dict.items():
        print(f"The '{l}' character was found {c} times")

def word_count(file):
    words = len(file.split())
    return words

def char_count(file):
    text_string = file.lower()
    char_dict = {}
    for c in text_string:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def alph_only(file):
    text_string = file.lower()
    letter_dict = {}
    for c in text_string:
        if c.isalpha() == True:
            if c in letter_dict:
                letter_dict[c] += 1
            else:
                letter_dict[c] = 1 
    return letter_dict 

main()