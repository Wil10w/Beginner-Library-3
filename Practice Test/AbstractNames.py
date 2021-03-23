#Write a function called abstract_names. abstract_names
#should have one parameter: a list of lists. Each list will
#be a list of strings, each with a first name and a last
#name, and each with the same first name.
#
#For example, this could be one list of lists your function
#might receive:
#
# [["David Joyner", "David Tennant", "David Beckham"],
#  ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"],
#  ["Inés Sainz", "Inés Suarez", "Inés Melchor"]]
#
#abstract_names should return a dictionary. The keys to the
#dictionary should be the first names, and the values should
#be lists of the associated last names. The last names should
#be sorted alphabetically.
#
#For example, with the list above, the dictionary returned by
#abstract_names would be:
#
# {"David": ["Beckham", "Joyner", "Tennant"],
#  "Ananya": ["Agarwal", "Birla", "Chatterjee", "Roy"],
#  "Inés": ["Melchor", "Sainz", "Suarez"]}


#Write your function here!
def abstract_names(alistOfLists):
    #an empty dictionary
    adict = {}
    #we loop over the list of lists
    for i in alistOfLists:
        #we loop over each list inside that list
        for j in i:
            #we split the full name(j) into a list
            tempList = j.split()
            #I know that an error will occur on the first iteration
            try:
                #if not first time - append second name to list
                adict[tempList[0]].append(tempList[1])
            #if it  is the first time, we get an erro because the list doesn't exist.
            #we can't append to a list that isn't there.
            except KeyError:
                #so we create the list inside the dictionary
                adict[tempList[0]] = [tempList[1]]
        #snappy loop to sort each list alphabetically
        for i in adict.values():
            i.sort()
    #return the completed dictionary
    return adict






#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"David": ["Beckham", "Joyner", "Tennant"], "Ananya": ["Agarwal", "Birla", "Chatterjee", "Roy"], "Inés": ["Melchor", "Sainz", "Suarez"]}
names = [["David Joyner", "David Tennant", "David Beckham"], ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"], ["Ines Sainz", "Ines Suarez", "Ines Melchor"]]
print(abstract_names(names))


