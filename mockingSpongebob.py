import sys

def mock(word):
    transformed = ""
    # begin with lowercase letter if no extra arguement is provided, otherwise begin with uppercase letter
    index = 0 if len(sys.argv) == 2 else 1
    for character in word:
        if character.isalpha():
            character = character.lower() if index % 2 == 0 else character.upper()
            index = index + 1
        transformed += character
    return transformed

def main():
    # sys.stdin.isatty() returns false if there's something in stdin
    if not sys.stdin.isatty():
        for line in sys.stdin:
            sys.stdout.write(mock(line))
    elif len(sys.argv) >= 2:
        print(mock(sys.argv[1]))

main()
    
    