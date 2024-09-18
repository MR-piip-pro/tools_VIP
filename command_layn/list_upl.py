import time
from rich.console import Console


def list_upl():
    # The text that will be printed
    text = """
            ╔═════════════════════════════════════════════════════════════════════════╗
            ║ 1 ==>    git init                                                       ║
            ║═════════════════════════════════════════════════════════════════════════║
            ║ 2 ==>    git remote add origin ("https://github.com/"   /   /   ")      ║
            ║═════════════════════════════════════════════════════════════════════════║
            ║ 3 ==>    git pull origin main --allow-unrelated-histories               ║
            ║═════════════════════════════════════════════════════════════════════════║
            ║ 4 ==>    git branch -m master main                                      ║
            ║═════════════════════════════════════════════════════════════════════════║
            ║ 5 ==>    git add .                                                      ║
            ║═════════════════════════════════════════════════════════════════════════║
            ║ 6 ==>    git commit -m "Initial commit after reinitializing repository" ║
            ║═════════════════════════════════════════════════════════════════════════║
            ║ 7 ==>    git push -u origin main                                        ║
            ╚═════════════════════════════════════════════════════════════════════════╝
            
            ╔═══════════════════════════════════════════════════════════════╗
            ║ To damage the data of the first repository, Run this command. ║
            ║═════════════════════╔═══════════════╗═════════════════════════║
            ║                     ║  rm -rf .git  ║                         ║
            ║═════════════════════╚═══════════════╝═════════════════════════║
            ║         The commands were rewritten from the first            ║
            ╚═══════════════════════════════════════════════════════════════╝
        """
    # Color and time variables
    color = "bright_blue"  # The selected color of the text
    delay = 0.005  # The exact time between printing each letter
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


def list_upd():
    # The text that will be printed
    text = """
            ╔═════════════════════════════════════════════════════════════════════════╗
            ║ 1 ==>    git status                                                     ║
            ║═══════════════════════════════════════════════╔═════════════════════════║
            ║ 2 ==>    git add README.md                    ║ #File name "README.md"  ║
            ║═══════════════════════════════════════════════╚═════════════════════════║
            ║ 6 ==>    git commit -m "Updated README.md with new changes"             ║
            ║ ════════════════════════════════════════════════════════════════════════║
            ║ 7 ==>    git push origin main                                           ║
            ╚═════════════════════════════════════════════════════════════════════════╝
        """
    # Color and time variables
    color = "bright_blue"  # The selected color of the text
    delay = 0.005  # The exact time between printing each letter
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
    

def command_list_logo():
    # The text that will be printed
    text = """
 
        ██████╗ ██╗██╗██████╗     ██████╗ ██████╗  ██████╗         /\                /\\
        ██╔══██╗██║██║██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗       /  \\'. _ (\\_/) _ .'/ \\
        ██████╔╝██║██║██████╔╝    ██████╔╝██████╔╝██║   ██║       |.''._'--(o.o)--'_.''.|
        ██╔═══╝ ██║██║██╔═══╝     ██╔═══╝ ██╔══██╗██║   ██║        \\_ / `;=/ " \\=;` \\ _/
        ██║     ██║██║██║         ██║     ██║  ██║╚██████╔╝          `\\__| \\___/ |__/`
        ╚═╝     ╚═╝╚═╝╚═╝         ╚═╝     ╚═╝  ╚═╝ ╚═════╝                \\(_|_)/
                                                                           " ` "
                Version: 0.0.1 
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
    
def list_command():
    print("""
          \033[1;31m╔══════════════════════════════════════════════╗
          \033[1;31m║   \033[1;35m1  --> Upload  the project on github.      \033[1;31m║
          \033[1;31m║   \033[1;35m2  --> Updated the project on github.      \033[1;31m║
          \033[1;31m║   \033[1;35m3  --> List recall.                        \033[1;31m║
          \033[1;31m║   \033[1;35m0  --> Back to the back.                   \033[1;31m║
          \033[1;31m╚══════════════════════════════════════════════╝
          
          
          """)