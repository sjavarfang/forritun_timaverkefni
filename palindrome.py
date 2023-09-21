a_str = input()

# Complete the program below

#here we create a new string that is read backwards and store it, we do that with using slicing [::-1]
reversed_string = a_str[::-1]

#we check if the 2 strings match, if so we print "Palindrome!" if not we print "Nothing special about this string :("
if a_str == reversed_string:
    print("Palindrome!")

else:
    print ("Nothing special about this string :(")