def string_finder(tar_string, search_string):
    length1 = len(tar_string) - 1 # Gives the length of tar_string and (-1) for 0 position
    search_len1 = len(search_string) - 1 #  same as above

    tar_char = tar_string[length1] #    returns the last letter/number in tar_string
    search_char = search_string[search_len1]#   returns the last letter/numer in search_string



    quartered = int(length1 / 3) # gives the value of the first quarter of the string
    halfed = int(length1 / 2) # value of half
    threeQ = halfed + quartered # value of the last quarter of the string

    if search_string in tar_string: # searching string
        n = tar_string.find(search_string) # returning the location of search_string in tar_string
        if n in range(0, quartered): # if it's near the beginning...
            if search_string[0] == tar_string[0]:# if the first letters match it's the beginning.
                return 'Beginning'
            else:
                return 'Middle' #   otherwise is not at position 0.

        elif n in range(quartered, halfed): # If it's between quarter and half way..
            if tar_char != search_char: # and the last letter DON'T match...
                return "Middle" # it's middle
            else: # otherwise
                return 'End'
        elif n in range (quartered, threeQ): # Almost the same as above but covers any positions missed.
            if tar_char != search_char: #   if the last letters DON'T match...
                return 'Middle'
            else: # otherwise
                return 'End'
            #   NOTE: this string above could be updated to and fit into the one above it by changing line 22 from
            #         (quartered, halfed) to (quartered, threeQ) to cover the whole middle section of the string.

        elif n in range (0, length1):#  This catches small strings that my get through the above statements
            if tar_char == search_char:# if the end characters match...
                return 'End'
            else: # This was ready in case I needed to make a - if search_string[0] == tar_string[0]
                return ' beginning(unused'
    else:
        return 'Not found'# empty strings




print(string_finder("Georgia Tech", "Georgia"))
print(string_finder("Georgia Tech", "gia"))
print(string_finder("Georgia Tech", "Tech"))
print(string_finder("Georgia Tech", "Idaho"))
print(string_finder("cs1301", "1301"))
print(string_finder("cs1301", "13"))
