# Here we find the appendix number for a given character in a string

# First, we ask for the string and the character that we are looking for
a_str = input()
char_to_count = input()

# Here we create an empty string to store our numbers of where the characters are found in the string
char_check = ""

# Here we start a for loop that iterates through each character in the string and stores the appendix number.
for i in range(len(a_str)):
    if a_str[i] == char_to_count:
        char_check += str(i) + " "

# Then we print out the list
print(char_check)