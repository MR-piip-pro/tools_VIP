import time
from rich.console import Console
def command_list_7():
    # The text that will be printed
    text = """
                            ╔═══════════════════════╗
                            ║ instagram_master v1.0 ║
                            ╚═══════════════════════╝
╔═════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                         ║
║      Instainsane is an Shell Script to perform multi-threaded brute force attack        ║
║    against Instagram, this script can bypass login limiting and it can test infinite    ║
║  number of passwords with a rate of about 1000 passwords/min with 100 attemps at once.  ║
║                                                                                         ║
╚═════════════════════════════════════════════════════════════════════════════════════════╝

                            ╔═══════════════════════╗
                            ║        Features       ║
                            ╚═══════════════════════╝
                     ╔═══════════════════════════════════════╗
                     ║  Multi-thread (100 attempts at once)  ║
                     ╚═══╗      Save/Resume sessions      ╔══╝
                         ║  Anonymous attack through TOR  ║
                 ╔═══════╝      Check valid usernames     ╚══════╗
                 ║  Default password list (best +39k 8 letters)  ║
                 ╚════╗  Check and Install all dependencies  ╔═══╝    
                      ╚══════════════════════════════════════╝

                            ╔═══════════════════════╗
                            ║         Usage         ║
                            ╚═══════════════════════╝
╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║                             Before running the utility                                    ║
║             you need to install some necessary packages and programs such as Tor.         ║
║                                                                                           ║
║                             ╔═══════════════════════╗                                     ║
║                             ║  sudo apt-get update  ║                                     ║
║                             ╚═══════════════════════╝                                     ║
║                         ╔═══════════════════════════════╗                                 ║
║                         ║  sudo apt-get install tor -y  ║                                 ║
║                         ╚═══════════════════════════════╝                                 ║
║                                                                                           ║
║                           Download the file from the link                                 ║
║                                                                                           ║
║   ╔═══════════════════════════════════════════════════════════════════════════════╗       ║
║   ║                                                                               ║       ║
║   ║  https://mega.nz/file/i6wUiYDT#HxuccJzkE77M_pntR48E3YxrW1rLZcmjewl4IHVqu0c    ║       ║
║   ║                                                                               ║       ║
║   ╚═══════════════════════════════════════════════════════════════════════════════╝       ║
║                                                                                           ║
║                Navigate to the instagram_mastar folder that you cloned                    ║
║                                                                                           ║
║                             ╔═══════════════════════╗                                     ║
║                             ║  cd instagram_master  ║                                     ║
║                             ╚═══════════════════════╝                                     ║
║                                                                                           ║
║                     Install requirements (Curl, Tor, Openssl)                             ║
║                                                                                           ║
║                             ╔═══════════════════════╗                                     ║
║                             ║  chmod +x install.sh  ║                                     ║
║                             ╚═══════════════════════╝                                     ║
║                             ╔═══════════════════════╗                                     ║
║                             ║   sudo ./install.sh   ║                                     ║
║                             ╚═══════════════════════╝                                     ║
║                                                                                           ║
║           Grant executive permissions to the file that you are going to run               ║
║                                                                                           ║
║                          ╔═════════════════════════════╗                                  ║
║                          ║   chmod +x instainsane.sh   ║                                  ║
║                          ╚═════════════════════════════╝                                  ║
║                           ╔═══════════════════════════╗                                   ║
║                           ║   sudo ./instainsane.sh   ║                                   ║
║                           ╚═══════════════════════════╝                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝
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