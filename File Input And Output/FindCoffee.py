#Write a function called "find_coffee" that expects a
#filename as a parameter. The function should open the
#given file and return True if the file contains the word
#"coffee". Otherwise, the function should return False.
#
#Hint: look up the read() method if you want to do this
#more simply than you might do with readline().


#Write your function here!
def find_coffee(aFile):
    input_file = open(aFile, 'r')# open file
    coffee = input_file.read()# taking all the data from the file and saving it to a variable
    input_file.close()# closing the file
    if 'coffee' in coffee:# if the word 'coffee' is in the variable above named coffee
        return True # return true
    else:
        return False# if it isn't in the variable




#You can test your function with the provided files named
#"coffeeful.txt" and "coffeeless.txt". With their original
#text, the lines below should print True, then False. You
#may also edit the files by selecting them in the drop
#down in the top left to try your code with different
#input.
print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))




