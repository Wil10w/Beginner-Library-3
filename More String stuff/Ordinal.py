#   this function turn the character into its ASCII and then checks to see if it falls
#   into the range listed below. It then returns True of False.

def valid_char(character):
    convert_num = ord(character)

    if convert_num in range(33, 127):
        return True
    else:
        return False






print(valid_char("a"))
print(valid_char(" "))
print(valid_char("!"))
print(valid_char("☺"))

