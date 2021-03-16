#Recall last exercise that you wrote a function, word_lengths,
#which took in a string and returned a dictionary where each
#word of the string was mapped to an integer value of how
#long it was.
#
#This time, write a new function called length_words so that
#the returned dictionary maps an integer, the length of a
#word, to a list of words from the sentence with that length.
#If a word occurs more than once, add it more than once. The
#words in the list should appear in the same order in which
#they appeared in the sentence.
#
#For example:
#
#  length_words("I ate a bowl of cereal out of a dog bowl today.")
#  -> {3: ['ate', 'dog', 'out'], 1: ['a', 'a', 'i'],
#      5: ['today'], 2: ['of', 'of'], 4: ['bowl'], 6: ['cereal']}
#
#As before, you should remove any punctuation and make the
#string lowercase.
#
#Hint: To create a new list as the value for a dictionary key,
#use empty brackets: lengths[wordLength] = []. Then, you would
#be able to call lengths[wordLength].append(word). Note that
#if you try to append to the list before creating it for that
#key, you'll receive a KeyError.


#Write your function here!
def length_words(astring):
    ###############################
    #these strips and replaces are a bit too much, but I couldn't think or find a better way to
    #format the string before splitting it into a list.
    astring = astring.lower()
    astring = astring.replace(', ', ' ')
    astring = astring.replace("'", '')
    astring = astring.strip('?')
    astring = astring.strip('!')
    astring = astring.strip()
    astring = astring.strip('.')
    #words is the name of the list that holds the split string
    words = astring.split()
    ################################
    #we have an empty variable to count the num of letters in each word
    count = 0
    #an empty Dictionary to hold the data
    adict = {}
    #we iterate through the list at the words as a whole ("Good")
    for i in words:
        #we reset the var to zero for every word.
        count = 0
        # we place i into a perminent variable, as the value of i doesn't seem to
        #cross into the nested loop.
        theWord = i
        #nested loop that iterates over ever letter in i ("g", "o", "o", "d")
        for j in i:
            #count each letter
            count += 1
        #
        try:
            adict[count].append(theWord)
        except KeyError:
            adict[count] = [theWord]

    return adict





#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
#The keys may appear in a different order, but within each
#list the words should appear in the order shown above.
print(length_words("She borrowed the book from him many years ago and hasn't yet returned it."))
