from tools.Repeat_messages import Repeat_messages
from tools.list_command import list_command
from tools.logo import logo_1
from tools.crypto import main
from taym.clear_os import clear_os

from command_layn.command_1 import command_list_1 
from command_layn.command_2 import command_list_2
from command_layn.command_4 import command_list_4
#from command.command_7 import command_list_7
#from command.command_8 import command_list_8
#from command.command_9 import command_list_9

from tools.upd_and_udl import upd_and_upl

#from os import system
clear_os()
# Call the logo and Menu function
logo_1()
list_command()
# List of correct commands
valid_commands = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "clear", "-h"]

while True:
    # Print the message to the user
    print("\033[1;35m┌──", ("\033[1;35m(MR@piip@pro)"))
    command = input("\033[1;35m└─$\033[1;33mcommand: \033[1;37m")
    
    # If the user enters "exit" exits the program
    if command.lower() == "exit":
        exit()
    # Check if the command is in the correct command list
    if command in valid_commands:
        try:
            # Execute the function associated with the command
            if command == "clear":
                clear_os()
            elif command == "1":
                command_list_1()
            elif command == "2":
                command_list_2()
            elif command == "3":
                upd_and_upl()
            elif command == "4":
                command_list_4()
            elif command == "5":
                Repeat_messages()
            elif command == "6":
                main()
            elif command == "7":
                print("7")
            elif command == "8":
                print("8")
            elif command == "9":
                print("9")
            elif command == "0":
                list_command()
        except Exception as e:
            print("command execution failed:", str(e))
    else:
        print("command is not found")
