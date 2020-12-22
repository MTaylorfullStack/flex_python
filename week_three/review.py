# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

# declare a function accepting a list as a parameter
    # declare that dictionary
    # loop through the list
        # if current value is less than min
            # current value is min
        # if current value is greater than max
            # current value is new max
        # add current value to our sumtotal
    # retrieve length
    # calculate avg
    # return dictionary

def ultimate_analysis(my_list):
    analysis = {
        'sum_total':0,
        'minimum': my_list[0],
        'maximum': my_list[0]
    }
    for i in range(len(my_list)):
        if my_list[i] < analysis['minimum']:
            analysis['minimum']=my_list[i]
        if my_list[i] > analysis['maximum']:
            analysis['maximum']=my_list[i]
        analysis['sum_total']+=my_list[i]
    analysis['length']=len(my_list)
    analysis['average']=analysis['sum_total']/len(my_list)
    return analysis

print(ultimate_analysis([2,4,6,8,10,12]))


