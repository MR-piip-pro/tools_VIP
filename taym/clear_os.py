import os
from os import system
# Clear the screen based on the system used
def clear_os():
    if os.name == 'nt':
        system("cls")
    else:
        system("clear")