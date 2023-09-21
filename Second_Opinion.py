total_seconds_str = input()  # Do not change this line.

# Convert to hours, minutes and seconds.

total_seconds_int = int(total_seconds_str)
hours = total_seconds_int // 3600
minutes = (total_seconds_int // 60) % 60
seconds = total_seconds_int % 60

print(hours, ":", minutes, ":", seconds)  # Do not change this line.
