#Write a function called one_dimensional_booleans.
#one_dimensional_booleans should have two parameters:
#a list of booleans called bool_list and a boolean called
#use_and. You may assume that bool_list will be a list
#where every value is a boolean (True or False).
#
#The function should perform as follows:
#
# - If use_and is True, the function should return True if
#   every item in the list is True (simulating the and
#   operator).
# - If use_and is False, the function should return True if
#   any item in the list is True (simulating the or
#   operator).


#Write your function here!
def one_dimensional_booleans(alist,boolean):
    length = len(alist)# gives us the length of the list so we can check it against the count
    count = sum(alist)# counts the number of True booleans in the list

    if boolean is True and count == length:# it's looking for all True by checking that count and length are the same
        return True

    if boolean is False and count >0:# is looking for a single True bool in the list. 
        return True
    else:
        return False




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False.
print(one_dimensional_booleans([True, True, True, True, True,True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))
print(one_dimensional_booleans([True, True, True], True))




