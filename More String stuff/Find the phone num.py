def find_phone_number(string):
    newList = string.split() # splitting the string up into a list
    n = ''
    for i in newList: # looping through the list
        if i.isnumeric():#  if it is a number...
            if len(i) == 10:#   if there are 10 numbers
                n += i #    adds the 10-digit numbe to n

    return n








print(find_phone_number("hello 4049876543 goodbye"))
print(find_phone_number("7705551234 this is alex"))
print(find_phone_number("doh ray me abc 123 its 6789123456"))