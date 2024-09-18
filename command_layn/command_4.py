import time
from rich.console import Console
def command_list_4():
    # The text that will be printed
    text = """
            
        The file contains 5 images:
            
        Download link:
            
                    " https://mega.nz/file/j2QjBbaY#jaFGsHEwSGrZ1VDvaFmS-NiSKhpJpwItSmQvVh9z-Vg "
                    
        """
    # Color and time variables
    color = "bright_blue blink"  # The selected color of the text
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