#Write a function called write_1301 which will write a file
#in the format described in Coding Problem 4.4.2. The
#sample.cs1301 file has been included to refresh your
#memory. Your function should accept two arguments:
#A string of a filename to write to, and a list of tuples.
#You can assume that each tuple will have the following
#format:
#
#(int, str, int, int, float)
#
#Each tuple will represent a line in the file, and each
#item in the tuple should correspond to the
#assignment number, the assignment name, the student's
#grade, the total possible number of points, and the
#assignment weight respectively.


#Write your function here!
def write_1301(afile, alistOfTups):
    #open file ready to write
    outputfile = open(afile, 'w')
    # loop over the list of tuples
    for tup in alistOfTups:
        #an empty string to concat the items in the tup
        astring = ''
        #turn the iterated tup into it's own list (I don't know why, I just did. I could probably just concat
        # from the tuple)
        alist = list(tup)
        #counting up from 0 to 4 so we can take every indexed item and add  it to a string
        for i in range(0, 5):
            #adding i from alist and concat it to astring while adding a space
            astring += str(alist[i]) + ' '
            #stripping the space from the end of the string
            astring.strip()
            #printing it to file without \n as print always starts on a new line
        print(astring, file=outputfile)







#The code below will test your function. It's not used
#for grading, so feel free to modify it! You may check
#output.cs1301 to see how it worked.
tuple1 = (1, "exam_1", 90, 100, 0.6)
tuple2 = (2, "exam_2", 95, 100, 0.4)
tupleList = [tuple1, tuple2]
write_1301("Outputcs1301.txt", tupleList)