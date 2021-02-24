#Write a function called "load_file" that accepts one
#parameter: a filename. The function should open the
#file and return the contents.#
#
# - If the contents of the file can be interpreted as
#   an integer, return the contents as an integer.
# - Otherwise, if the contents of the file can be
#   interpreted as a float, return the contents as a
#   float.
# - Otherwise, return the contents of the file as a
#   string.
#
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, anything you read from a file is
#   initially interpreted as a string.


#Write your function here!
def load_file(aFile):
    outputFile = open(aFile, 'r')# opening file in read only mode
    loadedData = ''# creating an empty variable for the data from the file

    for line in outputFile: #   looping over the open file
        loadedData += line # adding the info from the loop
    outputFile.close()# remembering to close the file like a good boy
    try:
        int(loadedData)# checking if the string can be converted into an int
        return int(loadedData)# if True, we return the variable as an Int
    except ValueError:# otherwise it throws up a ValueError and we enter another error handle
        try:# this is the next error handle
            float(loadedData)#  checking to see if the variable can be convcerted into a float
            return float(loadedData)# if True, we return the var as a float
        except ValueError:# if not, we enter the 3rd error handle
            str(loadedData) # if the variable is a string
            return str(loadedData)# we return a string



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))