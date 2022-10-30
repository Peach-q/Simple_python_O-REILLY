#part_3_simple_python

sec = 60
min = 60

second_per_hour = min * sec
second_per_day = second_per_hour * 24

other_time = second_per_day / second_per_hour
other_second_time = second_per_day // second_per_hour

print(second_per_hour, second_per_day, other_time, other_second_time)