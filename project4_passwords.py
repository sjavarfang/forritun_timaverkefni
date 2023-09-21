min_password_length = 6
max_password_length = 20
quit = "q"

valid_passwords = 0
invalid_passwords = 0
password_attempts = 0

password = input()

while password != quit:
    password_attempts += 1
    string_length = len(password)

    if string_length < min_password_length or string_length > max_password_length:
        print(f"{password}: Invalid length.")
        invalid_passwords += 1
    else:
        lowercase = any(ch.islower() for ch in password)
        uppercase = any(ch.isupper() for ch in password)
        numeric = any(ch.isdigit() for ch in password)

        lowercase_missing = not lowercase
        uppercase_missing = not uppercase
        numeric_missing = not numeric

        if lowercase_missing:
            print(f"{password}: Missing lower case letter.")
        
        if uppercase_missing:
            print(f"{password}: Missing upper case letter.")
        
        if numeric_missing:
            print(f"{password}: Missing numeric letter.")
        
        if lowercase and uppercase and numeric:
            print(f"{password}: Valid password of length {string_length}.")
            valid_passwords += 1
        else:
            invalid_passwords += 1

    password = input()

print(f"You tried {password_attempts} passwords, {valid_passwords} valid, {invalid_passwords} invalid.")
