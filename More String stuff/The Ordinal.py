# this is a program that takes an integer and returns the number (as a string) with an Ordinal fixture (st, nd, rd, th)

def to_ordinal(n):
    n_string = str(n) # this turns n from an int to a string
    num_length = len(n_string) - 1 # length of string
    last_n = n_string[num_length] # we get the last character in the string with the length.
    secondlast_num = num_length - 1 # the sencond last so we can check for 11, 12, 13, ( 1st, 11th, 2nd, 12th etc)


    if last_n == '1': # if the final num is string character 1
        if n_string[secondlast_num] == '1': # If the second num is also a 1 (checking for 11, 12, 13)
            if num_length == 0: #   checking to see if it's a single digit
                return n_string + 'st'
            else: # if it is a double (or triple) digit...
                return n_string + 'th'
        else:# I have no idea what this does hahahaha
            return n_string + 'st'
    elif last_n == '2':#    this checks for the character 2
        if n_string[secondlast_num] == '1':#    checks to see if adding second last num makes 12
            return n_string + 'th'
        else:#  otherwise it's a 2 and return...
            return n_string + 'nd'
    elif last_n == '3':#    this checks for the character 3
        if n_string[secondlast_num] == '1':#    checks to see if adding second last num makes 13
            return n_string + 'th'
        else: # othewise... it's 3, 23,33
            return n_string + 'rd'
    else: # still don't know why I have added this.
        return n_string + 'th'


print(to_ordinal(1))
print(to_ordinal(2))
print(to_ordinal(123))
print(to_ordinal(4))
print(to_ordinal(5))
print(to_ordinal(111))
print(to_ordinal(121))
print(to_ordinal(12))