def find_color(string):
    string = string.replace('rgb', '') # all these 'replace' functions are removing the 'rgb' and '()' from string
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace(',', '')

    newList = string.split() #  makes a list so it keeps the numbers separate.
# dominant colors
    for i in newList:
        if int(newList[0]) > (int(newList[1]) and int(newList[2])):
            if int(newList[0]) == int(newList[1]):
                return 'yellow'
            elif int(newList[1]) < (int(newList[0]) and int(newList[2])):
                return 'purple'
            elif (int(newList[0]) and int(newList[1])) > int(newList[2]):
                return 'green'
            else:
                return 'red'


        if int(newList[1]) > (int(newList[0]) and int(newList[2])):
            if int(newList[1]) == int(newList[2]):
                return 'teal'
            else:
                return 'green'

        if int(newList[2]) > (int(newList[0]) and int(newList[1])):
            if int(newList[2]) == int(newList[0]):
                return 'teal'
            else:
                return 'blue'

#

#equal parts
        if int(newList[0]) == int(newList[1]):
            if int(newList[2]) < int(newList[0]) and int(newList[1]):
                return 'yellow'
            elif int(newList[2]) > int(newList[0]) and int(newList[1]):
                return ' this could be anything'

        if int(newList[0]) == int(newList[2]):
            if int(newList[1]) < (int(newList[0]) and int(newList[2])):
                return 'purple'
            elif int(newList[1]) > (int(newList[0]) and int(newList[1])):
                return ' im not sure yet'


        if int(newList[1]) == int(newList[2]):
            if int(newList[0]) < (int(newList[1]) and int(newList[2])):
                return 'god knows2'
            elif int(newList[0]) > (int(newList[1]) and int(newList[2])):
                return ' God knows'

        # grey
        if int(newList[0]) == int(newList[1]) == int(newList[2]):
            return 'gray'

    return newList


print(find_color("rgb(125, 50, 75)"))# red
print(find_color("rgb(125, 17, 125)"))# teal
print(find_color("rgb(217, 217, 217)")) #gray
print(find_color("rgb(0, 217, 217)"))# green
print(find_color("rgb(217, 217, 217)")) #gray
print(find_color("rgb(100, 0, 0)")) #red
print(find_color("rgb(100, 100, 0)")) #yellow
print(find_color("rgb(0, 50, 50)")) #teal
print(find_color("rgb(10, 0, 10)")) #purple
print(find_color("rgb(136, 175, 56)")) #green
