alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_cipher_encrypt(text, offset) -> str:
    text = text.lower()

    encrypted_text = ""

    for char in text:
        new_index = None
        if alphabet.index(char) + offset >= len(alphabet):
            new_index = (alphabet.index(char) + offset) - len(alphabet)
        else:
            new_index = alphabet.index(char) + offset

        encrypted_text += alphabet[new_index]

    return encrypted_text


def caesar_cipher_decrypt(text, offset) -> str:
    text = text.lower()

    encrypted_text = ""

    for char in text:
        new_index = alphabet.index(char) - offset
        encrypted_text += alphabet[new_index]

    return encrypted_text
