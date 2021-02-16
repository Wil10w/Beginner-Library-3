#Write a function, called lucky_sevens, that takes in one
#parameter, a list of integers, and returns True if the list
#has three '7's  in a row and False if the list doesn't.
#
#For example:
#
#  lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
#
#Hint: As soon as you find one instance of three sevens, you
#could go ahead and return True -- you only have to find it
#once for it to be True! Then, if you get to the end of the
#function and haven't returned True yet, then you might
#want to return False.


#Write your function here!
def lucky_sevens(alist):
    count = 0

    for i in alist: # looping through the items in loop (not range 0,1,2,3 etc)

        if count == 2:# i started with the highest number in the count (checks 3, then 2, then 1) to prevent bugs
            if i == 7:# if the num is 7 and the count is 2 (this 7 will make it 3)
                return True # end with true
            else: # this is here to end the count if there are only 2 in a row.
                count = 0 # reset to zero incase there is a 7 then three 7s further in the list

        elif count == 1: # if there is already one in the list and..
            if i == 7: # this 7 is also the next number in the list...
                count += 1# add to the count (count should be 2 now)
            else:
                count = 0# otherwise reset to zero (happens if it's a single 7

        elif i == 7:# if the num is 7
            count +=1# add 1 to the counter and continue with the loop

    return False # otherwise end it with a false.

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))