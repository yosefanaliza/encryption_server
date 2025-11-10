

def fence_cipher_encrypt(text: str) -> str:
    text = text.replace(" ", "")

    rail1 = ""
    rail2 = ""
    
    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]
    
    return rail1 + rail2


def fence_cipher_decrypt(text: str) -> str:
    decrypted_text = ""
    
    mid = len(text) // 2 + len(text) % 2
    rail1 = text[:mid]
    rail2 = text[mid:]

    for i in range(mid):
        decrypted_text += rail1[i]
        if i < len(rail2):
            decrypted_text += rail2[i]

    return decrypted_text