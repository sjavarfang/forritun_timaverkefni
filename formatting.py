a_str = float(input())

#here we use formatting, the :12 determens that it should be formatted with 12 characthers and is right-justified
#.2f tells us that it shall be a float with 2 decimal points
formatted_float = "{:12.2f}".format(a_str)

print(formatted_float)