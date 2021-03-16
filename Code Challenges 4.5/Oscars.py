#Write a function called most_oscars, which takes in one
#parameter, a dictionary. This dictionary maps names to the
#number of Academy Awards for which they have been nominated.
#This function should return a tuple containing the name and
#number of nominations for the person who has the most
#nominations.
#
#You may assume there will not be a tie for the actor with
#the most nominations (although there may be other ties in
#the list).


#Write your function here!
def most_oscars(adict):
    #first we name two empty variables to hold the continually evolving high score.
    #so we determine highest between the number in highestNum and the current loop (data)
    #then if it is higher, it replaces the number in highestNum and we iterae again
    highestNum = 0
    NameOfStar = ''
    #loop over the dictioanry with both key and val
    for i in adict.items():
        #we unpack i (key and val) in name, data.
        name, data = i
        #a single if statement to check if data is larger than highestNum and if it is...
        #add name to NamOfStar and data to highestNum.
        if data > highestNum:
            highestNum = data
            NameOfStar = name




    # the higest score will be in the variable, as will the name of the celen be in the other.
    #then returning a tuple as requested.
    return NameOfStar, highestNum



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ('Meryl Streep', 20)
nominees = {'Christoph Waltz': 2, 'Oliver Stone': 3, 'Frank Capra': 6, 'David Lean': 7, 'Luise Rainer': 2, 'Frank Lloyd': 3}
print(most_oscars(nominees))




