def num_changer(string):
    length = len(string)
    length = int(length / 2)
    first = string[:len(string)//2] #   wow these to equations are perfect for finding the middle of an uneven letter
                                    #   count. I have no idea how it works :)
    second = string[len(string)//2:]
    return int(first) + int(second)






string_int = "123456"
result = num_changer(string_int)
print(string_int + " -> " + str(result))