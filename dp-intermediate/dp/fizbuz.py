# Challenge is to print fizz when multiples 3 input, 
# buzz for multiples of 5 and for for multiples of 3 and 5 
# it should be fizzbuzz in int format, 
# by user and  print all outputs, calculate time complexity.

# NOTE: Try to maintain O(1) and any SOLID principles

import time

n = int(input("Please add your input here : "))

def fizzbuzz(n):
    for i in range(1, n+1):
        if i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        elif i%3==0 and i%5==0:
            print("fizzbuzz")
        else:
            print(i)
    return "== END =="

def time_complexity(n):
    start = time.time()
    fizzbuzz(n)
    end = time.time()
    exec_time = start - end
    if exec_time == 0.0:
        print("Time Complexity is O(1)", exec_time, "seconds")
    else:
        print("Time Complexity is O(n)", exec_time, "seconds")
    return "== END =="

print(time_complexity(n))
        