def pluralize(inter, singular, plural):
    intToString = str(inter)
    output = ''
    if inter == 1:
        output = intToString + ' ' + singular
        return output
    if inter ==0:
         output = intToString + ' ' + plural
         return output
    else:
        output = intToString + " " + plural
        return output

print(pluralize(1, "cat", "cats"))
print(pluralize(7, "item", "items"))
print(pluralize(127, "octopus", "octopi"))