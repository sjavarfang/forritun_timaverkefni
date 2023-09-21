name = input()

#first we split the string in two parts, last name and first name
last_name, first_name = name.split(", ")

#here we want to take the first initial letter from the first name
#we do that by using [0] to identify what letter in the string we want to uppercase
first_initial = first_name[0].upper()

#then we want to capitlasise the first letter in the last name, we do that by using capatalize function
last_name = last_name.capitalize()

#then we create a new string by using what we split earlier and combine them again, both first_initail and last_name
formatted_name = f"{first_initial}. {last_name}"

print(formatted_name)