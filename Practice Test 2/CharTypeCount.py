#Write a function called count_types. count_types
#should take as input a single string, and return a
#dictionary. In the dictionary, the keys should be
#types of characters, and the values should be the
#number of times each type of character appeared in
#the string.
#
#The types of characters that should be handled (and
#thus, the keys in the dictionary) are:
#
# - upper: the count of upper-case or capital letters
# - lower: the count of lower-case letters
# - punctuation: the count of punctuation characters.
#   You may assume this is limited to these punctuation
#   characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# - space: the count of spaces
# - numeral: the count of numerals, 0123456789
#
#All five keys should be in your dictionary no matter
#what; if there are no characters of the corresponding
#type, the value associated with the key would just be 0.
#
#For example:
#
#count_characters("aabbccc") ->
# {"upper": 0, "lower": 7, "punctuation": 0, "space": 0, "numeral": 0}
#count_characters("ABC 123 doe ray me!") ->
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
#
#HINT: If you're sing the ord() function, capitals of
#ordinals between 65 and 90; lower-case letters have
#ordinals between 97 and 122; numerals are between 48
#and 57; spaces are 32; all other numbers between 33
#and 126 are punctuations, and no character will have
#an ordinal outside that range.


#Write your function here!
def count_types(astring):
    #we create the full dictionary as we must return all Keys whether they are
    #in the string or not (value 0 if not)
    adict ={"upper": 0, "lower": 0, "punctuation": 0, "space": 0, "numeral": 0}
    #loop over every char in string
    for i in astring:

        #if i is lower, add to dict Key lower
        if i.islower():
            adict['lower'] = adict.get('lower', 0) + 1

        #if upper, add to key 'upper
        elif i.isupper():

            adict['upper'] = adict.get('upper', 0) + 1

        #if i is a space, add 1 to Key 'space'
        elif i.isspace():

            adict['space'] = adict.get('space', 0) + 1

        #if it's a number, add 1 to Key 'numeral'
        elif i.isnumeric():

            adict['numeral'] = adict.get('numeral', 0) + 1

        #if it isn;t one of the others, then it must be punctualtions, so a to 'Punctuation'
        else:

            adict['punctuation'] = adict.get('punctuation', 0) + 1

    return adict







#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"upper": 0, "lower": 7, "punctuation": 0, "spaces": 0, "numerals": 0}
#{"upper": 3, "lower": 8, "punctuation": 1, "spaces": 4, "numerals": 3}
print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))



