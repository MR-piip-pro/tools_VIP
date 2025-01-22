from command_layn.sypt_command import command_crypto_lobs
from command_layn.list_crypto_1 import list_1, list_2, list_3
from taym.clear_os import clear_os

def main():
    command_crypto_lobs()
    while True:
        # Call function to display the command options (assumed from the function name)
        
        
        # Get user input for choosing an option
        choice = input("\033[1;36m        Enter the option number:  \033[1;31m")

        # If user chooses to encrypt a file
        if choice == "1":
            list_1()
            
        # If user chooses to decrypt a file
        elif choice == "2":
            list_2()
        
        # If user chooses to generate a random password
        elif choice == "3":
            list_3()
        
        elif choice == "4":
            command_crypto_lobs()

        elif choice == "0":
            clear_os()
            return

        # If the user inputs an invalid option
        else:
            # Display an error message
            print("\033[1;31mAn invalid option.")

# End of the main function
