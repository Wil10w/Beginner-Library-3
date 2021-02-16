#Write a function called multiply_by_index. multiply_by_index
#should have one parameter, a list; you may assume every item
#in the list will be an integer. multiply_by_index should
#return a list where each number in the original list is
#multipled by the index at which it appeared.
#
#For example:
#
#multiply_by_index([1, 2, 3, 4, 5]) -> [0, 2, 6, 12, 20]
#
#In the example above, the numbers 1, 2, 3, 4, and 5 appear
#at indices 0, 1, 2, 3, and 4. 1*0 = 0, 2 * 1 = 2, 3 * 2 = 6,
#and so on.


#Write your code here!
def multiply_by_index(alist):
    count = 0#  a counter variable
    newList =[]# a new list to store the outcome
    outcome = 0 #   momentarily holds the outcome of i*count
    for i in alist: # loops over the list
        outcome = i * count #   does the math
        newList.append(outcome)# adds outcome to the end of the list.
        count += 1#   adds up from zero for the index reference.
                    # eg alist[2] = 0 + 1 (first loop) + 1 (second tinme)
    return newList






#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[0, 2, 6, 12, 20]
#[0, 7, 14, 21, 28, 35, 42]
#[0, 7, 74, 195, 36, 0, 330]
print(multiply_by_index([1, 2, 3, 4, 5]))
print(multiply_by_index([7, 7, 7, 7, 7, 7, 7]))
print(multiply_by_index([14, 7, 37, 65, 9, 0, 55]))
