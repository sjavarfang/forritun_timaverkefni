from function_lexicographical_order import precedes


# But for running the program interactively,
# you might want to do something like this:

first = input("Give me a string: ")
second = input("Give me another string: ")

result = precedes(first, second)

print(f"The string '{result}' has alphabetical precedence.")
