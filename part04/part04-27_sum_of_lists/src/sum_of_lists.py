# Write your solution here
def list_sum(list1: list, list2: list):
    list3 =[]
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    return list3
