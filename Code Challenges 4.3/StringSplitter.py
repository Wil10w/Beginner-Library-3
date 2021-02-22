#Write a function called string_splitter that replicates the
#function of the string type's split() method, assuming that
#we're splitting at spaces. string_splitter should take as
#input a string, and return as output a list of the
#individual words from the string, assuming that words were
#divided by spaces. The spaces themselves should not be in
#the list that your function returns.
#
#You may assume that there will never be more than one space
#in a row, and that the string will neither start nor end
#with a space. However, you should not assume there will
#always be a space.
#
#You may not use Python's built-in split() method.
#
#For example:
#
#  string_splitter("Hello world") -> ['Hello', 'world']


#Write your function here!
def string_splitter(astring):
    alist = []# make an empty list
    aword = ""# make and empty variable to capture the letters
    for letter in astring:# looping through the letters in the string

        if letter == ' ':#  if there is a space in the string, we've hit the end of a word
            alist.append(aword)#    and it's time to add it to the list
            aword = ''# resets the variable that captures the letters, so we don't get a mushed string of words
        else:
            aword += letter# this esle adds all the letters together and makes the words from the loop

    alist.append(aword)#    this appends any string that is left in the variable to the list
    return alist





#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ['Hello', 'world']
print(string_splitter("Hello world"))




