import random
import string
import pyperclip

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Welcoming
print(bcolors.OKBLUE + "Starting Password Generator...")
print("")

characters = {
    "Uppercases": string.ascii_uppercase,
    "Lowercases": string.ascii_lowercase,
    "Numbers": string.digits,
    "Symbols": string.punctuation,
}

while True:
    try:
        n = int(input("\tLength of Password: "))
        break
    except ValueError:
        print(bcolors.FAIL + "Entered value should be an integer only.")
        print("Restarting the program...")
        print(bcolors.OKBLUE + "")

print(bcolors.OKGREEN + "Select character types for the password:")

for i, char_type in enumerate(characters, 1):
    print(f"\t{i} --- {char_type}")

selected_indices = []
while True:
    try:
        selected_indices = [int(index) for index in input(
            "Enter the serial numbers of the character types (e.g., 1 3 4): "
        ).split()]

        # Check if all entered indices are valid
        if all(1 <= index <= len(characters) for index in selected_indices):
            break
        else:
            print(bcolors.HEADER + "Invalid serial number(s). Please try again.")
            print(bcolors.OKBLUE + "")
    except ValueError:
        print(bcolors.HEADER + "Invalid input. Please enter valid serial numbers.")
        print(bcolors.OKBLUE + "")

selected_types = [list(characters.keys())[index - 1] for index in selected_indices]

password_list = []
for i in range(n):
    char_type = selected_types[i % len(selected_types)]
    password_list.append(random.choice(characters[char_type]))

password = ''.join(password_list)
print(bcolors.HEADER + "Your password:", password)
pyperclip.copy(password)
print(bcolors.OKCYAN + "Your password is copied to your clipboard.")
