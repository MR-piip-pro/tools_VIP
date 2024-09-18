from command_layn.sypt_command import encrypt_file, decrypt_file, generate_random_string
from taym.clear_os import clear_os
def list_2():
    print("\033[1;35m════════════════════════════════════════════════════════════════════════════════")
    # Get the file path for encryption from the user
    file_path = input("\033[1;36m        Enter the path of the file to be encrypted: \033[1;31m")
    print("\033[1;35m════════════════════════════════════════════════════════════════════════════════")
    # Get the encryption password from the user
    password = input("\033[1;36m        Enter the password for encryption: \033[1;31m")
    # Call the encryption function
    encrypt_file(file_path, password)

def list_3():
    print("\033[1;35m════════════════════════════════════════════════════════════════════════════════")
    # Get the file path for decryption from the user
    file_path = input("\033[1;36m        Enter the path to the encrypted file: \033[1;31m")
    print("\033[1;35m════════════════════════════════════════════════════════════════════════════════")
    # Get the decryption password from the user
    password = input("\033[1;36m        Enter the password for decryption: \033[1;31m")
    # Call the decryption function
    decrypt_file(file_path, password)

def list_1():
    clear_os()
    # Display the password strength options to the user
    print("""
        \033[1;34m    Choose a password strength
        \033[1;34m ══════════════════════════════════
        \033[1;34m   64 or less is considered weak
        \033[1;34m ══════════════════════════════════

        \033[1;34m 1 - Good          :      ===>   \033[1;31m 64
        
        \033[1;34m 2 - Very good     :      ===>   \033[1;31m 128
        
        \033[1;34m 3 - Powerful      :      ===>   \033[1;31m 256 
        
        \033[1;34m 4 - Very powerful :      ===>   \033[1;31m 512
    """)
    # Get the user's choice for password strength
    ke = input("\033[1;36m        Enter the option number:  \033[1;31m")

    # Set the length of the password based on the user's choice
    if ke == "1":
        ke = 64
    elif ke == "2":
        ke = 128
    elif ke == "3":
        ke = 256
    elif ke == "4":
        ke = 512
    else:
        # If the input is invalid, display an error message and exit the function
        print("\033[1;31m       An invalid option.")
        return

    # Generate a random password of the selected length
    random_value = generate_random_string(ke)
    clear_os()
    # Display the generated password to the user
    print(f"""\033[1;31m Random password: 
    
\033[1;35m {random_value} 

    """)
