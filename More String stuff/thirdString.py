def third_character(string):
    string_length = len(string)

    if string_length < 3:
        return 'Too short'
    else:
        return string[2]



print(third_character("CS1301"))
print(third_character("Georgia Tech"))
print(third_character("GT"))
