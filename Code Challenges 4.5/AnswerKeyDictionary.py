#Recall in an earlier problem you were given two lists: one
#list was a student's answers to a test, and the other was
#the answer key. Your goal was to return a score
#representing the number of problems the student got correct.
#
#Let's do that again, but with dictionaries instead of lists.
#Write a function called calculate_score. calculate_score
#should take two parameters: a dictionary of student answers
#and a dictionary of correct answers. Both dictionaries should
#have integers as their keys, and one-character strings as
#their values.
#
#calculate_score should count how many questions the student
#got right. Or, in more precise terms, calculate_score should
#count how many keys for which the associated value is the
#same in the student's dictionary and in the answer key
#dictionary.
#
#As before, it is possible that there will be more answers in
#one than the other. This means that these answers don't
#belong to the same test! If that happens, return -1.


#Add your function here!


def calculate_score(adict, bdict):
    #the score variable checks for extra answers in student answers by
    # minusing itself from corect answers. this will give a reslt less than
    # 0 if there are more.
    score = (len(adict) - len(bdict))
    #if score does result in a 0 or less...
    if not  score == 0:
        #immediately return -1
        return -1
    #loops over the renge of correct answer from 1 to length and adds
    # one for the range of the dictionary.
    for i in range(1, len(bdict) + 1):
        #it i in both dictionaries are the same..
        if adict[i] == bdict[i]:
            #add 1 to score
            score +=1
    #return variable score
    return score




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3
student_answers = {1: 'C', 2: 'C', 3: 'E', 4: 'E', 5: 'C', 6: 'D', 7: 'A', 8: 'B', 9: 'A'}
correct_answers = {1: 'D', 2: 'B', 3: 'C', 4: 'E', 5: 'C', 6: 'D'}
print(calculate_score(student_answers, correct_answers))




