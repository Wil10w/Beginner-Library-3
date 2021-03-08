#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!
def get_grade(afile):
    #open file in read only
    outputfile = open(afile, 'r')
    #create an empty list
    alist = []
    #loop over lines in file
    for line in outputfile:
        #split them to make a list
        aline = line.split()
        #it says in the instructions that all info will always be in the right order.
        #so we can use index [0] numbers to specifically target and change them

        #change this index to an int
        fint = int(aline[0])
        #this one too
        sint = int(aline[2])
        #this one also
        tint = int(aline[3])
        # this index to a float
        afloat = float(aline[4])
        #this index is already, and expected to be a string
        astring = aline[1]
        #creating a tuple out of the variables above
        atup = (fint, astring, sint, tint, afloat)
        #appending all tuples into this list.
        alist.append(atup)
        #closing the file.
    outputfile.close()
    ###############################################
    #this is a new program

    #making a few variables.
    total = 0
    math = 0
    #looping through each tuple in the list.
    for tup in alist:
        # saving the new outcome to 'math' in every loop
        math = tup[2] / tup[3] * tup[4]
        #adding 'math to total so each iteration's math is saved
        total += math
        #returning the total times 100
    return str(total) *100





#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 91.55
print(get_grade("samplecs1301.txt"))
