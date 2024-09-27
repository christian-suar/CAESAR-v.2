message = "abcd efASDASDASDj hijk lmnop qrs tuv wx yz 0 1 2 345 6789 "
number = 5

def ceaser_cipher(text:str, shift: int):
    result = ""
    for char in text:
        if char.islower():
            char = char.upper()
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            result += char

    return result

def ceaser_decipher(secret_message, shift): 
    result = ""
    for char in secret_message:
        if char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) - shift - 48) % 10 + 48)
        else:
            result += char

    return result


print("#########################################################################################################")
print("Encrypted: ")
print(ceaser_cipher(message, number))

print()

secret_message = ceaser_cipher(message, number)
print("Decrypted (original message): ")
print(ceaser_decipher(secret_message, number))
print("#########################################################################################################")