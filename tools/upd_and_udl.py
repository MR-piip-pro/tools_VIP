from taym.clear_os import clear_os
from command_layn.list_upl import list_upl, list_upd, command_list_logo, list_command

def upd_and_upl():
    clear_os()
    command_list_logo()
    list_command()
    while True:
        malk = input("  >>>\033[1;34m Select a number please:  \033[1;35m")
        if malk == "1":
            list_upl()
        elif malk == "2":
            list_upd()
        elif malk == "3":
            list_command()
        elif malk.lower() == "0":
            clear_os()
            return
        else:       
            print("""\033[1;36m Invalid procedure. Please choose 1 or 2 or 0 Back to the back please.
                  
                  
                  """)
