#In the previous problem, you wrote a function that would
#convert text like "abcd efgh ijkl" into "AbCd eFgH IjKl".
#
#In the previous problem, you could assume the original
#string would be all lower-case, with no punctuation.
#
#Revise your function so that it no longer makes these
#assumptions. It should leave any punctuation marks or
#numerals unchanged, and it should change the case of
#every letter at an even index. That means if the letter
#is initially uppercase, it should be converted to lower
#case.
#
#For example: mock("Abcd. Efgh.. Ijkl!") would return
#"abCd. efGh.. IJkL!". The even-index letters (A, C, E, g,
#j, l) changed case, all other characters were unchanged.
#
#HINT: Lowercase letters always have an ordinal between
#97 ("a") and 122 ("z"). Uppercase letters always have an
#ordinal between 65 ("A") and 90 ("Z").


#Write your function here!
def mock(string):
    new_string = '' #   an empty string for collecting the loop results
    for index, i in enumerate(string): #    it is counting using index and checking letters in string using i
        if index % 2 == 0: # this equation checks to see if it INDEX is an even number
            if i.isupper():# checking to see if i is an uppercase letter
                new_string += i.lower() # if it is... it makes it lowercase
            elif i.islower():#  if the letter is lowercase...
                new_string += i.upper() # it changes it to uppercase
            else: # if it is neither
                new_string += i #   it returns the original character

        elif index % 2 != 0:
            new_string += i #    if it is not an even number it returns the original character


    return new_string


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "abCd. efGh.. IJkL!".

print(mock("Abcd. Efgh.. Ijkl!"))



