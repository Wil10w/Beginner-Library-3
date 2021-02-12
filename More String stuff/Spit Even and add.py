def num_changer(string):
    length = len(string) +1
    evens = string[1:length:2]
    odds = string[0] + string[2:length:2]
    return int(evens) + int(odds)





string_int = "123456"
result = num_changer(string_int)
print(string_int + " -> " + str(result))