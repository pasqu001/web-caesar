switchL = {
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
    "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
    "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
    "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
    "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
    "z": 25
}
def alphabet_position(letter):
    return (switchL.get(letter.lower()))

def rotate_character(char, rot):
    if char.isupper():
        char_numb = alphabet_position(char)
        get_numb = (char_numb + rot) % 26
        for key, value in switchL.items():
            if value == get_numb:
                return key.upper()
    else:
        char_numb = alphabet_position(char)
        get_numb = (char_numb + rot) % 26
        for key, value in switchL.items():
            if value == get_numb:
                return key


def rotate_string(text, rot):
    new_string = ""
    for i in text:
        if i.isalpha():
            new_string += rotate_character(i, rot)
        else:
            new_string += i
    return new_string


def main():
    from sys import argv
    message = input("Yo, what is your message:\n")
    rotateBy = int(argv[1])
    print(rotate_string(message, rotateBy))

if __name__ == "__main__":
    main()
