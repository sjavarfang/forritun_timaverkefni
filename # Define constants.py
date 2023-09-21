# Define constants
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 20
QUIT_COMMAND = "q"

# Initialize counters for valid and invalid passwords
valid_passwords = 0
invalid_passwords = 0

while True:
    # Get user input
    password = input("Enter a password (or 'q' to quit): ")

    # Check if the user wants to quit
    if password == QUIT_COMMAND:
        break

    # Check password length
    if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
        print("Password length must be between 6 and 20 characters.")
        invalid_passwords += 1
        continue

    # Check for at least one lowercase letter, one uppercase letter, and one numeric letter
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_numeric = any(char.isdigit() for char in password)

    if not (has_lowercase and has_uppercase and has_numeric):
        print("Password must contain at least one lowercase letter, one uppercase letter, and one numeric letter.")
        invalid_passwords += 1
    else:
        print("Password is valid.")
        valid_passwords += 1

# Print the summary
print("Summary:")
print(f"Total passwords entered: {valid_passwords + invalid_passwords}")
print(f"Valid passwords: {valid_passwords}")
print(f"Invalid passwords: {invalid_passwords}")
