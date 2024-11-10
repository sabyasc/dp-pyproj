# Challenge is to find largest int by user input
# and print all outputs, calculate time complexity.

import time

def largest_int(input_int):
    data = max(input_int)
    return data

user_input = input("Please enter your input comma seperated :")

input_int = user_input.split(",")
input_int = [float(x) if '.' in x else int(x) if x.isdigit() else x for x in input_int]

data = largest_int(input_int)
print("Largest integer is :", str(data) if data else "No data found")

def time_complexity():
    start = time.time()
    largest_int(user_input)
    end = time.time()
    execution_time = start - end
    if execution_time == 0.0:
        print("Time Complexity is O(1)", execution_time, "seconds")
    else:
        print("Time Complexity is O(n)", execution_time, "seconds")
    return "== END =="

print(time_complexity())
