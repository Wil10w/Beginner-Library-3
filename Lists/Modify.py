#Write a function called modify_list. modify_list will
#take one parameter, a list. It should then modify the
#list in the following ways, in this order:
#
# - Sort the list (using the default sort method).
# - Reverse the order of the list.
# - Delete the last three items of the list.
# - Removes one instance the integer 7 from the list, if
#   it's present.
# - Double the values of the first and third items in
#   the list.
#
#It should then return the resulting list. You may assume
#the list will start with at least six items.
#
#Hint: Remember Python is 0-indexed. The second item
#does not have an index of 2.
#
#Hint 2: Remember, the list.remove() function removes items
#by value, not by index. Note also that if the item you're
#trying to remove is not found in the list, remove() will
#throw an error: so, you'll want to avoid that one way or
#another!


#Write your code here!
def modify_list(l):
    l.sort() # sorting numerically

    l.reverse()#  reversing - highest to lowest

    del l[-3:]# deleting the last three indexed
    try: # try statemen here to bypass errors from not finding 7
        l.remove(7) # removing first iteration of 7
    except:
        pass
    l[0] = l[0] * 2 # doubles the 1 number in the list
    l[2] = l[2] * 2 # doubles the 3 number in the list

    return l



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[178, 81, 75.0, 4, 3.141592653589793, 3]
import math
print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))



