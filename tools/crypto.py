#crpto.py

from command_layn.sypt_command import encrypt_file, decrypt_file, command_crypto_lobs

def main():
    command_crypto_lobs()
    
    choice = input("\033[1;36mEnter the option number: \033[1;31m")

    
    if choice == "1":
        print("\033[1;34m═════════════════════════════════════════════════════════════════════════════════════════")
        file_path = input("\033[1;36mEnter the path of the file to be encrypted: \033[1;31m")
        print("\033[1;34m═════════════════════════════════════════════════════════════════════════════════════════")
        password = input("\033[1;36mEnter the password for encryption: \033[1;31m")
        print("\033[1;34m═════════════════════════════════════════════════════════════════════════════════════════")
        encrypt_file(file_path, password)
    elif choice == "2":
        print("\033[1;34m═════════════════════════════════════════════════════════════════════════════════════════")
        file_path = input("\033[1;36mEnter the path to the encrypted file: \033[1;31m")
        print("\033[1;34m═════════════════════════════════════════════════════════════════════════════════════════")
        password = input("\033[1;36mEnter the password for decryption: \033[1;31m")
        print("\033[1;34m═════════════════════════════════════════════════════════════════════════════════════════")
        decrypt_file(file_path, password)
    else:
        print("\033[1;31mAn invalid option.")
    return


