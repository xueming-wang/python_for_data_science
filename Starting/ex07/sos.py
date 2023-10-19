import sys

def ft_morse_encode(str: str) -> str:
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": "·---",
        "K": "-·-",
        "L": "·-··",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": "·--.",
        "Q": "--.-",
        "R": "·-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": "·--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": "·----",
        "2": "··---",
        "3": "···--",
        "4": "····-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    try:
        if len(sys.argv) != 2:
            raise AssertionError
        if not str.isalnum() or str.isspace():
            raise AssertionError
        string = str.upper()
        morse_str = " ".join(NESTED_MORSE[c] for c in string)
        print(morse_str)
    except AssertionError:
        print("AssertionError: the arguments are bad")
        
def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
    else:
        ft_morse_encode(sys.argv[1])


if __name__ == "__main__":
    main()

