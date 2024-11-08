# Challenge is to find any duplicate in given input 
# in any format e.g. str, int, float, double ...etc and
# remove those duplicates and measure the time complexity, 
# print all outputs.

import time

def remove_duplicates(input_list):
    count_map = {}
    duplicates = []
    non_duplicates = []
    
    # Loop for counting data from input
    for item in input_list:
        if item in count_map:
            count_map[item] += 1
        else:
            count_map[item] = 1

    # Loop for fetching duplicate
    for item1, count1 in count_map.items():
        if count1 > 1:
            duplicates.append(item1)
    
    # Loop for fetching non duplicate
    for item2, count2 in count_map.items():
        if count2 == 1:
            non_duplicates.append(item2)
    
    return duplicates, non_duplicates
            
user_input = input("Please provide your input here seperated by comma :")
print("Original text:", str(user_input))
input_list  = user_input.split(',')
input_list = [int(x) if x.isdigit() else x for x in input_list]

duplicates = remove_duplicates(input_list)
print("Duplicates and Non Duplicates :", str(duplicates) if duplicates else "No Duplicates found")

def time_complexity():
    start = time.time()
    remove_duplicates(user_input)
    end = time.time()
    execution_time = start - end
    if (execution_time == 0.0):
        print("Time Complexity is O(1) : ", execution_time, "seconds")
    else:
        print("Time Complexity is O(n) : ", execution_time, "seconds")

print(time_complexity())
