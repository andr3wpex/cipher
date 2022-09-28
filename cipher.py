import string
alphabet = list(string.ascii_lowercase)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar()


def user_inputs():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet) + 1:
        shift = shift - (len(alphabet))

    return list(text), shift


def encrypt(text, shift, *direction):
    encrypted = []
    for char in text:
        if char in alphabet:
            # char is a letter
            idx = alphabet.index(char) + shift
            if idx > len(alphabet) - 1:
                idx = idx - (len(alphabet) - 1)
            encrypted.append(alphabet[idx])
        else:
            encrypted.append(char)
    return (''.join(encrypted))

def main():
    text, shift = user_inputs()
    secret = encrypt(text, shift)
    print(secret)

if __name__ == '__main__':
    main()
