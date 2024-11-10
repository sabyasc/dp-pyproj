# Challenge is to find longest str by user input
# and print all outputs, calculate time complexity.

import time

def longest_string(input_text):
    data = max(input_text, key=len)
    return data

user_input = input("Please enter your input comma seperated :")

input_text = user_input.split(",")
input_text = [float(x) if '.' in x else int(x) if x.isdigit() else x for x in input_text]

data = longest_string(input_text)
print("Longest string is :", str(data) if data else "No data found")

def time_complexity():
    start = time.time()
    longest_string(user_input)
    end = time.time()
    execution_time = start - end
    if execution_time == 0.0:
        print("Time Complexity is O(1)", execution_time, "seconds")
    else:
        print("Time Complexity is O(n)", execution_time, "seconds")
    return "== END =="

print(time_complexity())
