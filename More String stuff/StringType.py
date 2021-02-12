def string_type(string):
    stringLen = len(string)
    fullStops = string.count('.')
    spaces = string.count(' ')
    exMarks = string.count('!')
    newLine = string.count('\n')

    if not string:
        return 'empty'
    if stringLen ==1:
        return 'character'
    if spaces >= 3 and (fullStops >= 2 or exMarks >=1) and newLine >= 1:
        return 'page'
    if spaces >= 3 and fullStops >= 2:
        return 'paragraph'

    if spaces > 2 and (fullStops >= 1 or exMarks >= 1):
        return 'sentence'
    if stringLen >= 2:
        return 'word'




print(string_type(""))
print(string_type("!"))
print(string_type("CS1301."))
print(string_type("This is too many cases!"))
print(string_type("There's way too many ostriches. Why are there so many ostriches. The brochure said there'd only be a few ostriches."))
print(string_type("Paragraphs need to have multiple sentences. It's true.\nHowever, two is enough. Yes, two sentences can make a paragraph."))