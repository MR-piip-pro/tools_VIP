import time
from rich.console import Console
def part_1():
    # The text that will be printed
    text = """
                            . .  ,  ,
                            |` \/ \/ \,',
                            ;          ` \/\,.
                           :               ` \,/               /\                /\\    
                           |                  /               /  \\'. _ (\\_/) _ .'/ \\
                           ;                 :                |.''._'--(o.o)--'_.''.|    
                          :                  ;                 \\_ / `;=/ " \\=;` \\ _/
                          |      ,---.      /                    `\\__| \\___/ |__/`
                         :     ,'     `,-._ \                         \\(_|_)/
                         ;    (   o    \   `'                          " ` "
                       _:      .      ,'  o ;
                      /,.`      `.__,'`-.__,
                      \_  _               \ 
                     ,'  / `,          `.,'
               ___,'`-._ \_/ `,._        ;
            __;_,'      `-.`-'./ `--.____)
         ,-'           _,--\^-'
       ,:_____      ,-'     \                 ██████╗ ██╗██╗██████╗     ██████╗ ██████╗  ██████╗   
      (,'     `--.  \;-._    ;                ██╔══██╗██║██║██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗        
      :    Y      `-/    `,  :                ██████╔╝██║██║██████╔╝    ██████╔╝██████╔╝██║   ██║   
      :    :       :     /_;'                 ██╔═══╝ ██║██║██╔═══╝     ██╔═══╝ ██╔══██╗██║   ██║   
      :    :       |    :                     ██║     ██║██║██║         ██║     ██║  ██║╚██████╔╝  
       \    \      :    :                     ╚═╝     ╚═╝╚═╝╚═╝         ╚═╝     ╚═╝  ╚═╝ ╚═════╝   
        `-._ `-.__, \    `.                                        v.1.0.21
           \   \  `. \     `.                           Destroy      the       chat
         ,-;    \---)_\ ,','/
         \_ `---'--'" ,'^-;'
         (_`     ---'" ,-')
         / `--.__,. ,-'    \ 
         )-.__,-- ||___,--' `-.
        /._______,|__________,'\ 
        `--.____,'|_________,-'
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
