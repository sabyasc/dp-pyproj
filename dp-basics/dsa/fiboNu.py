# Challenge is to implement DSA - fibonacci series and
# print all outputs, calculate time complexity.

# Logic - Fibonacci series is a maths mechanism which sums next proceding numbers, e.g = 1, 2, 3, 5, 8.... etc

import time

user_input = int(input("Please enter your value here : "))

def fibonacci(user_input):
    fib = []
    a,b = 0,1
    for _ in range(user_input):
        fib.append(a)
        a,b = b, a+b
    print("Fibonacci series is :", fib)
    return fib

def time_complexity():
    start = time.time()
    fibonacci(user_input)
    end = time.time()
    execution_time = start - end
    if execution_time == 0.0:
        print("Time Complexity is O(1)", execution_time, "seconds")
    else:
        print("Time Complexity is O(n)", execution_time, "seconds")
    return "== END =="

print(time_complexity())

