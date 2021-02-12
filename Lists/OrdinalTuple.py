# Remember asciitable.com from an earlier exercise? We're
# going to use it again. Remember, ordinal values for
# characters are given in the 'Dec' column of asciitable.com.
#
# Write a function called character_info. character_info will
# take as input a string with only one character. It should
# return a 3-tuple with three pieces of information:
#
# - In the first spot, the character itself.
# - In the second spot, the ordinal value of the character,
#   obtained using the ord() function (e.g. ord("a") -> 97).
# - In the third spot, what type of character it is: either
#   "letter", "number", or "punctuation".
#
# You may assume that anything that is not a letter (either
# upper or lower case) or a number is punctuation. You may
# also assume the ordinal will be between 32 (" ") and 126
# ("~").


# Write your function here!
def character_info(char):

    ordinalVal = ord(char) # get the ASCII number of 'char'
    charType = '' # empty string
    if ordinalVal in range(48, 57):#    if the ASCII number is between 48 and 57...
        charType = 'number' #   Print number

    elif ordinalVal in range(97, 122):# #    if the ASCII number is between 97 and 122...
        charType = 'letter'# print Letter
    elif ordinalVal in range(65, 90):#  #    if the ASCII number is between 65 and 90...
        charType = 'letter'#    print letter (this is for uppercase)
    else: #if it's not a number or letter
        charType = 'punctuation' # print punctuation

    myTup = char, ordinalVal, charType # collect all variables in this tuple
    return myTup

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ('q', 113, 'letter')
# ('7', 55, 'number')
# ('`', 96, 'punctuation')
print(character_info("A"))
print(character_info("7"))
print(character_info("`"))




