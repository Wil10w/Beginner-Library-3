
def in_parentheses(string):


    first_para = string.find('(')
    second_para = string.find(')')

    if string:
        if (first_para == -1 and second_para >= 1):
            return "Closed ) only"
        if second_para == -1 and first_para >= 1:
            return "Open ( only"
        if second_para < first_para:
            return "Closed ) before ( open"
        if first_para == -1 and second_para == -1:
            return "No parentheses here!"
        if first_para < second_para:
            return string.split('(', 1)[1].split(')')[0]
    else:
        return ''












print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(in_parentheses("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
print(in_parentheses("Open ( only"))
print(in_parentheses("Closed ) only"))
print(in_parentheses("Closed ) before ( open"))
print(in_parentheses(""))









