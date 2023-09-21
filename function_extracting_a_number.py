# extract_first_number_from_string definition goes here


def extract_first_number_from_string(input_str):
    int_in_string = ""
    for m in input_str:
        if m.isdigit():
            int_in_string += m
        elif int_in_string:
            return int(int_in_string)
    if int_in_string:
        return int(int_in_string)  
    return -1  
