# PRODIGY_CS_01

## Task-01: Caesar Cipher Python Implementation
### Introduction
The PRODIGY_CS_01 project implements the Caesar Cipher algorithm, a simple encryption technique used to encode and decode messages by shifting each letter in the text by a fixed number of positions in the alphabet. This program allows users to input a plaintext message along with a shift value, and it outputs the encrypted message (ciphertext) and can also decrypt it back to the original text using the same shift value. The goal of this project is to demonstrate the basic principles of cryptography through hands-on implementation in Python.

### How It Works

1. **User Input**: The user provides a plaintext message.
2. **Shift Value**: A shift value (key) is applied to shift each letter of the message.
3. **Encryption**: The program outputs the encrypted message (ciphertext).
4. **Decryption**: The same shift value is used to decrypt the ciphertext back to the original message.

### Sample Dataset

| Input Message      | Shift Value | Encrypted Output  | Decrypted Output |
|--------------------|-------------|-------------------|------------------|
| `HELLO WORLD`      | `3`         | `KHOOR ZRUOG`     | `HELLO WORLD`    |
| `CYBERSECURITY`    | `5`         | `HDGJWXJXZWNFY`   | `CYBERSECURITY`  |
| `ATTACK AT DAWN`   | `7`         | `HAAPJH HA KHDU`  | `ATTACK AT DAWN` |

### Features
- **Encrypt**: Converts the plaintext message into ciphertext by shifting characters.
- **Decrypt**: Converts the ciphertext back to the original message using the same shift value.

---

## How to Run the Program

Follow these steps to run the Python program:

### 1. Install Python (If Not Installed)
Before running the code, ensure that Python is installed on your machine. If not, follow these steps:
- Go to the [official Python website](https://www.python.org/downloads/).
- Download and install the latest Python version for your operating system (Windows or macOS).
- During installation, make sure to check the box **“Add Python to PATH”** before clicking **"Install Now."**

### 2. Save the Python Code
1. Open a text editor (such as **VS Code**, **Notepad++**, or **PyCharm**).
2. Copy the Python code and paste it into the text editor.
3. Save the file as `caesar_cipher.py` on your computer (ensure the file extension is `.py`).

### 3. Open a Command Prompt or Terminal
- **Windows**:
  - Press `Windows + R`, type `cmd`, and press `Enter` to open the Command Prompt.
- **macOS**:
  - Open the **Terminal** from your Applications or using a shortcut (e.g., `Command + Space` on macOS).

### 4. Navigate to the Folder Containing the Code
Using the `cd` (change directory) command, navigate to the folder where the Python script is saved. For example:
- **Windows**:
  ```cmd
  cd C:\Users\YourName\Documents\PythonScripts
### 5. Run the Python Script & Input Data

Once you are in the correct directory, run the script by typing:

python caesar_cipher.py

When prompted, enter the message you want to encrypt and the shift value. For example:

    Message: HELLO WORLD
    Shift Value: 3

The program will output the encrypted and decrypted messages.
### Expected Output Example:

| Input Message   | Enter shift Value | Encrypted Message | Decrypted Message|
|-----------------|-------------------|-------------------|------------------|
| `HELLO WORLD`   | `3`               | `KHOOR ZRUOG`     | `HELLO WORLD`    |

### **Author**  
👤 **Ahmed Qatar**  
🔗 [LinkedIn](https://www.linkedin.com/in/ahmedsalahqatar)  
🌐 [Ahmed Qatar's Sec Lab](https://ahmedqatar-seclab.renderforestsites.com/)
