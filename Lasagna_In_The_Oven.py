degrees_f_str = input()
# Convert degrees_f_str to an integer.
degrees_f_int = int(degrees_f_str)
# Convert to °C.
convert_to_c =(degrees_f_int - 32) * (5/9)

# Round to nearest whole number.
degrees_c = round(convert_to_c)

print(degrees_c)