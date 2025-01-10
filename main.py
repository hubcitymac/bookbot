def main():
    file_path = r"github.com/hubcitymac/bookbot/books/frankenstein.txt"
    #text = get_text(file_path)


def get_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    string = get_text(text).lower()
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter_dict ={}
    for letter in letters:
        letter_dict[letter] = string.count(letter)
    sorted_dict = {key: val for key, val in sorted(letter_dict.items(), key = lambda ele: ele[1], reverse = True)}
    for char in sorted_dict:
        print (f"The {char} letter was found {sorted_dict[char]} times")

def report(text):
    print (f"Begin report of {text}")
    print (f"{word_count(get_text(text))} words appear in the document")
    char_count(text)
    print ("End of report")

main()
report(r"github.com/hubcitymac/bookbot/books/frankenstein.txt")