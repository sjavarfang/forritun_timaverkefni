number = int(input())  # Do not change this line

# Fill in the missing code below

if number == 0:
    print("The number does not contain 7.")
else:
    no_7_found_yet = False
    while number != 0:
        remainder = number % 10
        if remainder == 7:
            no_7_found_yet = True
            break
        number //= 10

    if no_7_found_yet:
        print("The number contains 7.")
    else:
        print("The number does not contain 7.")