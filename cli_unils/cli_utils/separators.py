
def print_separator():
    """Print a line of 30 asterisks."""
    print("*" * 30)

def print_char_separator(char):
    """Print a line of 30 of the given character."""
    print(char * 30)

def print_custom_separator(char, length):
    """Print a custom line of any character with specified length."""
    if length <= 0:
        print("")
        return
    print(char * length)


def print_labeled_separator(label, char="*", width=30):
    """Print a separator with a label centered inside it."""
    
    text = f" {label} " 
    print(text.center(width, char))


def print_boxed_text(message, char="*"):
    """Print a message surrounded by a full box."""
    
    width = len(message) + 4
    border = char * width

    print(border)
    print(f"{char} {message} {char}")
    print(border)


def print_color_animal():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

    # Colored ASCII art
    art = f"""
{BLUE}                      _         _
 .-""-.          ({YELLOW} )-"```"-({YELLOW} )          .-""-.
 / {GREEN}O O{BLUE}  \\          /         \\          /  {GREEN}O O{BLUE} \\
|{GREEN}O .-.{BLUE}  \\        /   {RED}0 _ 0{BLUE}   \\        /  .-. {GREEN}O{BLUE}|
\\ (   )  '.    _|     ({RED}_){BLUE}     |     .'  (   ) /
 '.`-'     '-./ |             |`\\.-'     '-'.'
   \\         |  \\   \\     /   /  |         /
    \\        \\   '.  '._.'  .'   /        /
     \\        '.   `'-----'`   .'        /
      \\   .'    '-._        .-'\\   '.   /
       |/`          `'''''')    )    `\\|
       /                  (    (      ,\\
      ;                    \\    '-..-'/ ;
      |                     '.       /  |
      |                       `'---'`   |
      ;                                 ;
       \\                               /
        `.                           .'
          '-._                   _.-'
    jgs    __/`"  '  - - -  ' "`` \\__
         /`            /^\\           `\\
         \\(          .'   '.         )/
          '.(__(__.-'       '.__)__).'{RESET}
"""
    print(art)

# Call the function
print_color_animal()