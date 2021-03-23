#Write a function called find_median. find_median
#should take as input a string representing a filename.
#The file corresponding to that filename will be a list
#of integers, one integer per line. find_median should
#return the median of the numbers in the file.
#
#If there is an odd number of values in the file, then
#find_median will return the middle value from the numbers
#in the file after they're sorted.
#
#If there is an even number of values in the file, then
#find_median should return the average of the two middle
#values after they're sorted.
#
#For example, in the dropdown in the top left you'll find a
#file named FindMedianInput.txt. There are 19 numbers in
#this file, so the median is the value at index 10 after
#sorting them: 16.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.


#Write your function here!


def find_median(afile):
    #open file
    inputfile = open(afile, 'r')
    #an emply list
    alist = []
    #variable to counter the lines in the file
    counter = 0
    #we loop over the lines in the file
    for line in inputfile:
        #we add to counter variable
        counter += 1
        #we remove the new line from 'line'
        line = line.replace('\n', '')
        #we append 'line' to the list and make it a float
        alist.append(float(line))
    # after the loop is complete we sort the list
    alist.sort()
    #we make a var with the length of the list so our code below doesn't get to complicated
    listLength = len(alist)
    #close the file as we don't need it now.
    inputfile.close()
    # if the list length is even
    if listLength % 2 == 0:
        #find the middle num
        left = (len(alist) //2)
        #find the number below middle
        right = (len(alist) //2) - 1
        #add both numbers together and divide by 2
        outcome = (alist[left] + alist[right]) / 2
        #return outcome
        return outcome
    #if list length is odd
    if listLength % 2 != 0:
        #find the middle number in the list
        findTheMiddle = (counter) // 2
        #return the number associated with the middle index
        return alist[findTheMiddle]




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16
print(find_median("FindMedianInput.txt"))


