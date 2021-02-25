#Write a function called "angry_file_finder" that accepts a
#filename as a parameter. The function should open the file,
#read it, and return True if the file contains "!" on every
#line. Otherwise the function should return False.
#
#Hint: there are lots of ways to do this. We'd suggest using
#either the readline() or readlines() methods. readline()
#returns the next line in the file; readlines() returns a
#list of all the lines in the file.


#Write your function here!
def angry_file_finder(afilename):
    output_file = open(afilename, 'r')# open file
    alist = output_file.readlines()# load file content into a list by using readlines()
    output_file.close()#    close the god damn file!!
    count = 0# a var for counting the lines in the file
    x = 0#   counting how many lines have '!'
    if not alist:# if no strings in file return False
        return False
    for line in alist:# iterating over the strings in the list
        count +=1#  adds one to for every line we iterate
        if "!" in line:#  if the line has a '!'
            x += 1# += 1

    return x == count





#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True
print(angry_file_finder("AngryFileFinderInput.txt"))




