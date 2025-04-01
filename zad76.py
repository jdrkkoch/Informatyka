def encrypt(text, key):
    text = list(text)  
    n = len(key)
    
    for i in range(len(text)):
        swap_pos = key[i % n] - 1 
        text[i], text[swap_pos] = text[swap_pos], text[i]
    
    return "".join(text)

def decrypt(text, key):
    text = list(text)
    n = len(key)

    inverse_key = [0] * n
    for i, k in enumerate(key):
        inverse_key[k - 1] = i + 1
    
    for i in range(len(text) - 1, -1, -1): 
        swap_pos = inverse_key[i % n] - 1
        text[i], text[swap_pos] = text[swap_pos], text[i]
    
    return "".join(text)

with open("szyfr3.txt", "r") as file:
    text = file.read().strip()  
    key = [6, 2, 4, 1, 5, 3]  

decrypted_text = decrypt(text, key)

with open("wyniki_szyfr3.txt", "w") as file:
    file.write(decrypted_text)
