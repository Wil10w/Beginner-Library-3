#Write a function called course_info that takes as input a
#list of tuples. Each tuple contains two items: the first
#item in each tuple is a student's name as a string, and the
#second item in each tuple is that student's age as an
#integer.
#
#The function should return a dictionary with two keys.
#The key "students" should have as its value a list of all
#the students (in other words, a list made from the first
#value of each tuple), in the original order in which they
#appeared in the list. The key "avg_age" should have as its
#value a float representing the average age of all the
#students in the list (in other words, the average of all
#the second items in the tuples).
#
#For example:
#
#  course_info([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avg_age": 20.5}
#
#Hint: Concentrate first on building the list of students
#and calculating the average age. Save creating the
#dictionary for last.


#Write your function here!
def course_info(listOfTups):
    #we make an empty list
    student =[]
    #create an empty variable
    average = 0
    #we loop over the tuples in the dict
    for tuple in listOfTups:
        #we use this really cool way of separating a tuple into to variables
        name, age = tuple
        #then add 'name' into the list
        student.append(name)
        #we add age to the empty variable
        average += age
    #we constuct a dictionary with the list(student) and find the average(averge) from the length
    #of the list(student)
    students = {'student': student, 'avg_age': average / len(student)}
    #we return student
    return students

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'avg_age': 20.5, 'students': ['Jackie', 'Marguerite']}
print(course_info([("Jackie", 20), ("Marguerite", 21)]))



