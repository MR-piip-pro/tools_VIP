import time
from rich.console import Console
def command_list_1():
    # The text that will be printed
    text = """
        This is a Tkinter-based application for managing system updates and installations,
        
        on a Kali Linux system. It provides a GUI to execute common commands,
        
        for updating the system, installing various tools, and managing packages.           

    Features

        ~ Update and Upgrade System: Updates the package list and upgrades installed packages.
    
        ~ Install Tor: Installs the Tor server for anonymous and secure web browsing.
    
        ~ Install Proxychains: Installs ProxyChains to force network connections through a series of proxies.
    
        ~ Install Code - OSS: Installs the open-source version of Visual Studio Code.
    
        ~ Install Airgeddon: Installs Airgeddon, a tool for network security testing.
    
        ~ Install Basics for Airgeddon: Installs additional tools required for Airgeddon.
    
        ~ Install Python3: Installs Python 3 on your Linux system.
    
        ~ Install List Password: Provides a link to download a list of passwords.

    Installation:
            
            Clone the repository:

               " git clone https://github.com/MR-piip-pro/AUUOSL.git "
            
            Username for:

                " MR-pro-pro "
                
            password git:
            
               " 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 "
    
            Navigate into the cloned directory:

                cd /home/kali/Downloads/AUUOSL
    
            Install required Tools packages:

                chmod +x test.sh
    
            Execution of orders:

                ./test.sh
    
            Run the application:

                python nano.py
                
     Usage:
    
        When you run the application, a main window will appear with options to perform various system updates and 
        
        installations. Each option opens a new window explaining the command and providing a button to execute it.
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