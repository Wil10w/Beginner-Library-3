#APA citation style cites author names like this:
#
#  Last, F., Joyner, D., & Burdell, G.
#
#Note the following:
#
# - Each individual name is listed as the last name, then a
#   comma, then the first initial, then a period.
# - The names are separated by commas, including the last
#   two.
# - There is also an ampersand and additional space before
#   the final name.
# - There is no space or comma following the last period.
#
#Write a function called names_to_apa. names_to_apa should
#take as input one string, and return a reformatted string
#according to the style given above. You can assume that
#the input string will be of the following format:
#
#  First Last, David Joyner, and George Burdell
#
#You may assume the following:
#
# - There will be at least three names, with "and" before
#   the last name.
# - Each name will have exactly two words.
# - There will be commas between each pair of names.
# - The word 'and' will precede the last name.
# - The names will only be letters (no punctuation, special
#   characters, etc.), and first and last name will both be
#   capitalized.


#Write your function below!
def names_to_apa(astring):
    #this formats the string so no extra spaces or punctuation makes it to the list
    astring = astring.replace('and', '')
    astring = astring.replace('  ', ' ')
    astring = astring.replace(', ', ',')
    #2 empty lsts
    blist = []
    #we split the string into alist
    alist = astring.split(',')
    #an emply variable
    output = ''
    #list for inside the loop
    templist = []
    #we loop over alist
    for i in alist:
        #and separate the full name into (this could have been done with .split())
        templist = i.split()
        #then we concat into apa format
        avar = templist[1] + ', ' + templist[0][0]+'.'','
        #and add to blist
        blist.append(avar)
    #we name an empty var
    avar = ''
    #we then loop over the length of blist minus the last index
    for i in range(0, len(blist) - 1):
        #we concat each index onto a string without the last one
       avar += blist[i] + ' '
    #a variable with the index of the final name.
    length = len(blist) - 1
    #we add a '&' to the incomplete string, then add the final name
    #so we have Name, L., & Last, F.
    avar += '& ' + blist[length]
    #return the string with the last character - so this Name, F. istead of Name, F.,
    return avar[:-1]
















#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Last, F., Joyner, D., & Burdell, G.
print(names_to_apa("First Last, David Joyner, and George Burdell"))


