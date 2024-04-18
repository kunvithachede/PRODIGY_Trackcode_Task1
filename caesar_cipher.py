def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            offset = ord(char) - start
            new_offset = (offset + shift) % 26
            new_char = chr(new_offset + start)
            if mode == "decrypt":
                new_offset = (offset - shift) % 26
                new_char = chr(new_offset + start)
            result += new_char
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher program!")
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value (1-25): "))
    mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    if mode == "encrypt":
        print("Encrypted message:", caesar_cipher(text, shift, mode))
    elif mode == "decrypt":
        print("Decrypted message:", caesar_cipher(text, shift, mode))
    else:
        print("Invalid mode selected. Please try again.")

if __name__ == "__main__":
    main()