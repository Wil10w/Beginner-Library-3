import types
def input_type(string):
    fullStops = string.count(".")
    numbers = string.isnumeric()
    isString = string.isalpha()




    if string == 'True' or string == 'False':
        return 'boolean'

    if fullStops:
        return 'float'
    if numbers and not fullStops:
        return 'integer'

    for i in string:
        if i.isalpha():
            return 'string'

    if isString or string == '':
        return 'string'



print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("yX+KIx:/"))