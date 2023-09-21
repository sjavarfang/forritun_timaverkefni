from function_is_substring import is_substring_of


# Now that you have learned about defining your own functions,
# it is a good time to introduce the following common convention.
# You can wrap your program inside a main function.
def main():
    # If you want the output to look exactly like in the problem statement,
    # you want to use this:

    first = input()
    second = input()
    result = is_substring_of(first, second)
    print(result)

    # But for running the program interactively,
    # you might want to do something like this:

  
main()
