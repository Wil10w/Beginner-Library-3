#Recall in the previous problem you counted the number of
#instances of a certain first name in a list of full names.
#You returned a dictionary with the name as the key, and the
#number of times it appeared as the value.
#
#Modify that code such that instead of having a count as the
#value, you instead have a list of the full names that had
#that first name. So, each key in the dictionary would still
#be a first name, but the values would be lists of names.
#Make sure to sort the list of names, too.
#
#Name this new function name_lists.


#Add your function here!
def name_lists(alistOfNames):

    alist = []
    b = ''
      
    for i in alistOfNames:

        b = i.split()
        alist.append(b[0])

        aDict = {}


    for word in alist:
        if word in aDict:
            pass
        else:
            aDict[word] =[]

    for i in aDict:
        for j in alistOfNames:
            if i in j:
                aDict[i].append(j)
            else:
                pass
    return aDict

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Fry', 'Shelba Odle'],
#'David': ['David Joyner', 'David Zuber'], 'Brenton': ['Brenton Joyner', 'Brenton Zuber'],
#'Maren': ['Maren Fry'], 'Nicol': ['Nicol Barthel']}

name_list =  ["Agnes Spangler", "Willy Cephas", "Waltraud Spangler",
              "Willy Spangler", "Waltraud Cephas", "Agnes Vineyard",
              "Waltraud Miltenberger", "Jody Miltenberger", "Burl Vineyard",
              "Luci Cephas", "Luci Spangler", "Agnes Miltenberger", "Burl Cephas"]
print(name_lists(name_list))
