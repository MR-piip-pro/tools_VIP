#sypt_command.py

import os
import time
from rich.console import Console
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def command_crypto_lobs():
    # The text that will be printed
    text = """
          ╔═══════════════════════════════════════════╗
          ║               Choose an option.           ║
          ║   1  -->    File encryption.              ║
          ║   2  -->    Decrypt a file.               ║
          ║   0  -->    Back to the back.             ║
          ╚═══════════════════════════════════════════╝
          
          
          """
    # Color and time variables
    color = "bright_blue"  # The selected color of the text
    delay = 0.001  # The exact time between printing each letter
    def slow_print_colored(text, color, delay=0.01):
        # Create a Console object for color printing
        console = Console()
        # Loop to repeat each letter in the text
        for char in text:
            # Print the character with the selected color without moving to a new line
            console.print(char, style=color, end='')  
            # Delay printing the character by the specified amount of time
            time.sleep(delay)
        print()  # Move to a new line after printing the entire text
    # Call the function with text passing, color, delay time
    slow_print_colored(text, color, delay)




def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key



def encrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    salt = os.urandom(16)
    key = generate_key(password, salt)
    nonce = os.urandom(12)
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()
    tag = encryptor.tag
    encrypted_file_path = f"{file_path}.enc"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(salt + nonce + tag + encrypted_data)
    print(f"تم تشفير الملف: {encrypted_file_path}")



def decrypt_file(file_path, password):
    with open(file_path, 'rb') as encrypted_file:
        file_data = encrypted_file.read()
    salt = file_data[:16]
    nonce = file_data[16:28]
    tag = file_data[28:44]
    encrypted_data = file_data[44:]
    key = generate_key(password, salt)
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce, tag),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    try:
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        decrypted_file_path = file_path.replace(".enc", "")
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        print(f"تم فك تشفير الملف: {decrypted_file_path}")
    except Exception as e:
        print(f"Decoding failure: {e}")
        
        
    