import sys

# Caesar Cipher Implementation
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Ensure shift stays within the alphabet range
            base = ord('a') if char.islower() else ord('A')
            new_char = chr(((ord(char) - base + shift_amount) % 26) + base)
            result += new_char
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

# Ensure the input prompt is displayed correctly
sys.stdout.flush()
sys.stdin.flush()

# Taking input from the user
message = input("Enter your message: ").strip()

# Handling invalid shift values
while True:
    try:
        shift_value = int(input("Enter shift value: ").strip())  # Strip removes extra spaces
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Encrypt the message
encrypted_message = caesar_cipher(message, shift_value)
print("Encrypted message:", encrypted_message)
