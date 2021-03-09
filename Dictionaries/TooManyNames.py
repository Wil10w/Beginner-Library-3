#Write a function called name_counts. name_counts will take
#as input a list of full names. Each name will be two words
#separated by a space, like "David Joyner".
#
#The function should return a dictionary. The keys to the
#dictionary will be the first names from the list, and the
#values should be the number of times that first name
#appeared.
#
#HINT: Use split() to split names into first and last.


#Add your function here!
def name_counts(listOfNames):
    alist = []
    #created an emplty list
    #iterated over input list(listOfNames)
    for i in listOfNames:
        #slit the iteration so the full name is separated
        b = i.split()
        alist.append(b[0])
        #added the first name to the new list
    #emply dictionary
    aDict ={}
    #looped over the new list
    for word in alist:
        #if word is already in the dictionary.
        if word in aDict:
            #plus one to that item
            aDict[word] += 1
         #else, make that make within the dictionary and give it a value of one
        else:
            aDict[word] = 1
    return aDict








#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': 5, 'Maren': 1, 'Nicol': 1, 'David': 2, 'Brenton': 2}
name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_counts(name_list))
