def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char  # Keep spaces and punctuation unchanged
    
    return result

# Get user input
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

# Encrypt the message
encrypted_text = caesar_cipher(message, shift_value, mode='encrypt')
print("Encrypted Message:", encrypted_text)

# Decrypt the message
decrypted_text = caesar_cipher(encrypted_text, shift_value, mode='decrypt')
print("Decrypted Message:", decrypted_text)
