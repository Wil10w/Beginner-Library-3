#Write a function called sum_lists. sum_lists should take
#one parameter, which will be a list of lists of integers.
#sum_lists should return the sum of adding every number from
#every list.
#
#For example:
#
# list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# sum_list(list_of_lists) -> 67


#Add your code here!
def sum_lists(list):
    result = 0 # creating a variable (not a list) as we want a single result.
    for alist in list: # looping through the list of lists... but first we...
        value = 0 # gotta make a variable for the next loop
        for integer in alist:# then we loop inside each list
            value += integer #take the value of each loop(iterate) and add it together
        result += value # take the added numbers from list and add them together with the results from the other lists

    return result





#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 78
list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum_lists(list_of_lists))