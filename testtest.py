def extract_first_number_from_string(input_str):
    int_in_string = ""
    for m in input_str:
        if m.isdigit():
            int_in_string += m
        elif int_in_string:
            return int_in_string

input_str = "There are 365 or 366 days in the year."
print(extract_first_number_from_string(input_str))