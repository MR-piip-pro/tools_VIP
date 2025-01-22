import random
import string
import os
import time
from rich.console import Console
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def command_crypto_lobs():
    text = """
          ╔═══════════════════════════════════════════╗
          ║            Choose an option.              ║
          ║       ══════════════════════════          ║
          ║   1  -->    Create a password.            ║
          ║   2  -->    File encryption.              ║
          ║   3  -->    Decrypt a file.               ║
          ║   4  -->    List recall.                  ║
          ║   0  -->    Back to the back.             ║
          ╚═══════════════════════════════════════════╝
          
    """
    color = "bright_blue"
    delay = 0.001

    def slow_print_colored(text, color, delay=0.01):
        console = Console()
        for char in text:
            console.print(char, style=color, end='')
            time.sleep(delay)
        print()

    slow_print_colored(text, color, delay)

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=500000,
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
    print("""
    
    """)
    print(f"\033[1;35m File encrypted: \033[1;35m {encrypted_file_path}")

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
            print("""
    
            """)
        print(f"\033[1;35m File decrypted: \033[1;35m {decrypted_file_path}")

    except Exception as e:
        print(f"\033[1;35m Decoding failure: \033[1;31m{e} \033[1;35m")
