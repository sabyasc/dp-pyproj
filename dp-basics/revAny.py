# Challenge is to reverse any given input in any format
# e.g. str, int, float... etc and 
# measure the time complexity, print all outputs.

import time

def reversed_string(user_data):
    text = str(user_data)
    print("Original Text : ", text)
    reversed_text = text[::-1]
    print("Reversed Text : ", reversed_text)
    return reversed_text

user_data = input("Please provide your Input in any format: ")

def time_complexity():
    start = time.time()
    reversed_string(user_data)
    end = time.time()
    execution_time = start - end 
    if(execution_time == 0.0):
        print("Time complexity is O(1) : ",  execution_time, "seconds")
    else:
        print("Time complexity is O(n) :", execution_time, "seconds")
    return " === Program Completed ==="
    
print(time_complexity())
