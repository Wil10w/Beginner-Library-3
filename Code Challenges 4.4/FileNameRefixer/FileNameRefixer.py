#You've been sent a list of names. Unfortunately, the names
#come in two different formats:
#
#First Middle Last
#Last, First Middle
#
#You want the entire list to be the same. For this problem,
#we'll say you want the entire list to be Last, First Middle.
#
#Write a function called name_refixer. name_refixer should have two
#parameters: an output filename (the first parameter) and the
#input filename (the second parameter). You may assume that every
#line will match one of the two formats above: either First Middle
#Last or Last, First Middle.
#
#name_refixer should write to the output file the names all
#structured as Last, First Middle. If the name was already structured
#as Last, First Middle, it should remain unchanged. If it was
#structured as First Middle Last, then Last should be moved
#to the front and a comma should be added after it.
#
#The names should appear in the same order as the original file.
#
#For example, if the input file contained the following lines:
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray
#
#...then the output file should contain these lines:
#Joyner, David Andrew
#Hart, Melissa Joan
#Cyrus, Billy Ray


#Add your code here!
def name_refixer(bfile, afile):
    #open the file
    outputfile = open(afile, 'r')
    # pull all data from file and place in list
    alist = outputfile.readlines()
    #close file
    outputfile.close()

    # create a variable for holding string concat
    names = ''
    #open bfile in write mode
    outputfile = open(bfile, 'w')
    #loop through the list with data
    for i in range(len(alist)):
        #if there is a comma, this means it's a surname first - correct format
        if ',' in alist[i]:
            # if the string is in correct format - strip white space and old '\n' and add new one to end
            names = alist[i].strip() + '\n'
            # write to file
            outputfile.write(names)

        else:
            #make a new lsit from i index of alist
            newList = alist[i].split()
            #rearrange the list so index 2 (surname) is first
            names = newList[2] + ', ' + newList[0] + ' ' + newList[1] + '\n'
            #write to file
            outputfile.write(names)
    #close file
    outputfile.close()



#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, output_file.txt should have the text:
#Joyner, David Andrew
#Hart, Melissa Joan
#Cyrus, Billy Ray
name_refixer("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

#If you accidentally erase input_file.txt, here's its original
#text to copy back in (remove the pound signs):
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray


