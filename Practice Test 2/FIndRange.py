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
def find_range(afile):
    #open file in read mode
    afilename = open(afile, 'r')
    #this variable is huge so we can definitely capture thr first number in the loop
    # ie - if I started the var at 100 and the first number in the file is 230, and this is
    # the smallest number, we will get an incorrect answer because the if statement couldn't
    #catch the smallest number - so i started it at a mil
    smallest = 1000000
    #this one is easy - it will definitely catch the first num in the loop
    largest = 0
    #we loop through the lines in the file
    for line in afilename:
        #the line is a string so we cut the '\n' away
        line = line.replace('\n', '')
        #change it to an integer
        line = int(line)
        # if it is greater than largest
        if line > largest:
            #it becomes largest
            largest = line
        #if it is less than smallest
        if line < smallest:
            #it becomes smallest
            smallest = line
    #close the file
    afilename.close()
    #return the tuple iwth the two variables
    return (smallest, largest)







#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (2, 37)
print(find_range("FindRangeInput.txt"))


