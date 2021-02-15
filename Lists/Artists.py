#We've learned a lot in this chapter. Let's try to use a lot
#of it for one final exercise.
#
#Write a function called sort_artists. sort_artists will
#take as input a list of tuples. Each tuple will have two
#items: the first item will be a string holding an artist's
#name, and the second will be an integer representing their
#total album sales (in millions).
#
#Return a tuple of two lists. The first list in the
#resulting tuple should be all the artists sorted
#alphabetically. The second list should be all the revenues
#sorted in descending numerical order.
#
#For example:
# artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
# sort_artists(artists) -> (["Elvis Presley", "Michael Jackson", "The Beatles"], [270.8, 211.5, 183.9])
#
#Notice that artists is a list of tuples (brackets first,
#then parentheses), but sort_artists outputs a tuple of
#lists (parentheses first, then brackets).
############################################
#   working it out
#   def sort_artists(list of tuples):
#   make tuple = ()
#   make list1 = []
#   MAKE LIST2 = []
#       Loop over List
#              loop over tuples
#                   if item is a string:
                #       append list 1
                #   if item is float:

      # sort lists

      # return as a tuple by floats, strings

#Write your function here!
def sort_artists(list_tup):

    names = [] #    make a list to store strings
    rev = []#   make a list to store floats

    for list in list_tup: # loop over tuple
        for item in list:#  loop over lists
                if (type(item) == float): # if item is a float
                    rev.append(item)#   add it to revenue (rev)
                else:#  otherwise
                    names.append(item)# it's a string and should be added to names

    names.sort() # default .sort alphabetically
    rev.sort(reverse=True)# sort using the reverse=True so the floats are from largest to smallest


    return names, rev # creates tuple when two variables are returned. In this case, 2 lists. 



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))



