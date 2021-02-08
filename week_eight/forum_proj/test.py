# all_forums=[
#     {'name':"Chess", 'desc': "A forum to talk chess"},
#     {'name': "Stock", 'desc': "trade and sell"}
# ]

# for forum in all_forums:
#     print(forum['name'])

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# declare the function, given a list
    # declare a sum
    # loop through the list
        # add values into sum
    # return sum

def sum_total(a_list):
    sum=0
    for i in range(len(a_list)):
        sum=sum+a_list[i]
    return sum

print(sum_total([50,50]))

