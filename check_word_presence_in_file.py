import sys
import re

"""
Does not match word
Example of file containing list of words OK test:
    hello, identity, nationality, name
Example of file containing list of words NOT OK test:
    hello, identity, nationality, help, world, test, name
File to compare to:
    hello my [name] is Celine
    I am writing scripts that I can reuse
    I gave you my identity.
    _test
    Do you know my nationality?
Output OK:
    OK
Output NOK:
    help not present in file-to-compare.txt
    world not present in file-to-compare.txt
    test not present in file-to-compare.txt
    NOT OK
    The following words are missing: ['help', 'world', 'test']
"""

def is_present(word, filename):
    sub_re = "\[?" + word + "\W*"
    return re.search("\s" + sub_re + "\s|\s" + sub_re + "$|^" + sub_re + "\s|^" + sub_re + "$", open(filename).read())

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3.x " + sys.argv[0] + " separator list-words-to-check-file file-to-compare-to")
        sys.exit()

    separator = sys.argv[1]
    list_words_file = sys.argv[2]
    filename = sys.argv[3]

    with open(list_words_file,'r') as f:
        list_words_string = f.read()
 
    list_words = list_words_string.split(separator)

    not_present_counter = 0
    not_present_words = []

    for word in list_words:
        word = word.strip()
        if not is_present(word, filename):
            not_present_counter += 1
            not_present_words.append(word)
            print(word + " not present in " + filename)
    
    if not_present_counter > 0:
        print("NOT OK")
        print("The following words are missing: " + str(not_present_words))
    else:
        print("OK")

