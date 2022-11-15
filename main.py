#calculate average value in list

def average(list):
    return sum(list)/len(list)

def calculate_average(list):
    list_length = 0
    for i in list:
        list_length += 1
    list_sum = 0
    for i in list:
        list_sum += i
    return list_sum/list_length

print(average([1,2,3,4,5,6,7,8,9,10]))
print(calculate_average([1,2,3,4,5,6,7,8,9,10]))


