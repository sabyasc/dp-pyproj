# Challenge is to find anagram using sorting mechanism
# for given input in any format e.g. str, int...etc and 
# print all outputs with calculated time complexity.

import time

user_data_1 = input("Please provide your first input here :")
user_data_2 = input("Please provide your second input here :")

def anagramSort(user_data_1, user_data_2):
    str1 = str(user_data_1)
    str2 = str(user_data_2)
    print("Original User given data : ", str1, str2)
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    sort_check = sorted(str1) == sorted(str2)
    
    if sort_check ==  True:
        print("String is Anagram")
    else:
        print("String is not Anagram")

def time_complexity():
    start = time.time()
    anagramSort(user_data_1,user_data_2)
    end = time.time()
    execution_time = start - end
    if (execution_time == 0.0):
        print("Time Complexity is O(1)", execution_time, "seconds")
    else:
        print("Time Complexity is O(n)", execution_time, "seconds")
    return "=== END ==="

print(time_complexity())

