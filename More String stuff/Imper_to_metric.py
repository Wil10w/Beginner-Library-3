def to_metric(string):
    num = ''
    word = ''

    for i in string: # looping through string
        if i.isnumeric():#  checking for numbers
            num += i # building a string with numbers
        if i == '.': # if it has a decimal (the strings are all numbers and decimals)
            num += '.' # adding the single decimal point to the number
        if i.isalpha():#    if it has letters
            word += i # add them to this variable

    gallons = 4546.09
    quarts = 1136.52
    pints = 568.26
    cups = 236.59
    ounces = 28.41
    tablespoons = 14.79
    teaspoons = 4.93


    if word == "gallons": # if the built string (word) is "gallon"
        output = float(num) * gallons# variable output does this math
    elif word == 'quarts':# if the built string (word) is "quarts"
        output = float(num) * quarts# variable output does this math
    elif word == 'pints':# if the built string (word) is "pints"
        output = float(num) * pints# variable output does this math
    elif word == 'cups':# if the built string (word) is "cups"
        output = float(num) * cups# variable output does this math
    elif word == 'ounces':# if the built string (word) is "ounces"
        output = float(num) * ounces# variable output does this math
    elif word == 'tablespoons':# if the built string (word) is "tablespoons"
        output = float(num) * tablespoons# same as the others
    elif word == 'teaspoons':# if the built string (word) is "teaspoons"
        output = float(num) * teaspoons#    you get the idea

    return round(output, 2)#    returns outcome to 2 decimal places


print(to_metric("7.0 cups"))
print(to_metric("2.0 tablespoons"))
print(to_metric("8.0 gallons"))
