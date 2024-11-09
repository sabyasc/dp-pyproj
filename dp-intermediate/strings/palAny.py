# Challenge is to find Palindrome for given input 
# in any format e.g. str, int...etc by user and 
# print all outputs, calculate time complexity.

# NOTE: Try to maintain O(1) and any SOLID principles

import time

userInput = input("Please add your input here :")

def palindrome(userInput):
    text = str(userInput).lower()
    print("Original Data :", text)
    reverse_text = text[::-1]
    if reverse_text == text:
        print("Input is Palindrome")
    else:
        print("Input is not Palindrome")
    return reverse_text

def time_complexity():
    start = time.time()
    palindrome(userInput)
    end = time.time()
    exceution_time = start - end
    if exceution_time == 0.0 :
        print("Time Complexity is O(1) :", exceution_time, "seconds")
    else:
        print("Time Complexity is O(n) :", exceution_time, "seconds")
    return "== END =="

print(time_complexity())
    