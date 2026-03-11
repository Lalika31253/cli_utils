
from cli_utils import (
    print_separator,
    print_char_separator,
    print_custom_separator,
    print_labeled_separator,
    print_boxed_text,
    print_color_animal
)

# Basic separator
print_separator()

# Character separators
print_char_separator("-")
print_char_separator("=")
print_char_separator("~")

# Custom length separators
print_custom_separator("*", 30)
print_custom_separator("-", 10)
print_custom_separator("#", 50)

# Labeled separator
print_labeled_separator("DONE", char="-", width=40)

# Boxed Text
print_boxed_text("Heelo World", "*")

print_color_animal()

