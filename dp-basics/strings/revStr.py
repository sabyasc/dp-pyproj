# Challenge is to reverse a simple string - "Hello World !!" and 
# measure the time complexity, print all outputs.

import time

def reversed_string():
    text = "Hello World !!"
    print("Original Text : ", text)
    reversed_text = text[::-1]
    print("Reversed Text : ", reversed_text)
    return reversed_text

def time_complexity():
    start = time.time()
    reversed_string()
    end = time.time()
    execution_time = start - end 
    if(execution_time == 0.0):
        print("Time complexity is O(1) : ",  execution_time, "seconds")
    else:
        print("Time complexity is O(n) :", execution_time, "seconds")
    return " === Program Completed ==="
    
print(time_complexity())
