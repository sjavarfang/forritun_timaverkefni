a_str = input()

# Complete the program below

#we create a new empty string that we want to store our new string in
inverted_str = ""

#we use for loop to check each character on a_str. 
#the .swapcase function swaps each case charater and it is then stored in our new string
for ch in a_str:
    inverted_str += ch.swapcase()

print(inverted_str)