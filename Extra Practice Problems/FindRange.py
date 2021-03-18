#Write a function called find_range. find_range should take
#as input a string representing a filename. The file
#corresponding to that filename will be a list of integers,
#one integer per line. find_range should return a tuple
#containing the smallest and largest numbers in the file
#(the smallest first, then the largest).
#
#For example, in the dropdown in the top left you'll find a
#file named FindRangeInput.txt. The smallest number in that
#file is 2, and the largest is 37. So, if you called
#find_range("FindRangeInput.txt"), the function would return
#(2, 37), a tuple with two integers.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.
#
#Hint: Remember, if you loop through all the lines in a file
#then you have to close and reopen the file to read it again,
#or by use file.seek(0) to start from the top. However, you
#can do this problem without having to read the file twice.


#Write your function here!
def find_range(afilename):
    #we open the file
    outfilename = open(afilename, 'r')
    #we create a variable for the largest num with a starting val of 0 so it captures the
    #first iteration and then all other values are checked against that.
    largest = 0
    #smallest var has to have an extremely high starting val so that the first iteration
    #captures the value - so if we set it to 0 and the actual lowest value was 1 - the
    # if statment below will never change the value in this variable because line is never less
    # than 0, so we start will a rediculous value so it will instantly change.
    smallest = 10000
    #loop through file
    for line in outfilename:
        #if line is greater than variable 'largest'
        if int(line) > int(largest):
            #line becomes the new 'largest'
            largest = line
        #else if line is less than 'smallest'
        elif int(line) < int(smallest):
            #line becomes the now 'smallest'
            smallest = line
    #return smallest and largest in a tuple
    return int(smallest), int(largest)



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (2, 37)
print(find_range("FindRangeInput.txt"))


