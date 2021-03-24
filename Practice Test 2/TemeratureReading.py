#Imagine you're writing the code for an intelligent
#temperature device. The device takes a measurement every
#10 seconds. However, some readings may come up invalid.
#We can assume based on operating conditions that all
#valid temperatures will be between 20 and 80.
#
#Write a function called average_temp. average_temp
#should have one parameter, a list of integers. The list
#represents a series of temperature measurements over the
#past several minutes.
#
#average_temp should return the average of all the last
#five _valid_ (greater than or equal to 20, less than or
#equal to 80) measurements.  Round the result to 1
#decimal place (you can use round(some_float, 1) to round
#to 1 decimal place).
#
#For example, if the list of measurements was this:
#
# [5, 62, 72, 102, 68, 75, 73, 3, 7, 79]
#
#average_temp would return 73.4: the last 5 valid
#measurements are (in reverse order) 79, 73, 75, 68, and
#72. (79 + 73 + 75 + 68 + 72) / 5 = 73.4.
#
#If there are fewer than five valid readings, return the
#averages of however many valid readings there are.


#Add your code here!
def average_temp(alist):
    #two empty variables for adding the numbers and one for outing the iterations
    adding = 0
    count = 0
    # looping through list in reverse
    for num in reversed(alist):
            #if count is still below 5
           if count != 5:
               # and if the number is over 20, under 80
               if num >= 20 and num <= 80:
                #add it to the variable
                adding += num
                #add to the count (maxing out at five)
                count += 1
                #Otherwise pass by and continue on.
               else:
                   pass
    # return average to 1 decimal
    return round(adding / count, 1)









#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 73.4, then 67.0 (on their own lines)
a_list = [5, 62, 72, 102, 68, 75, 73, 3, 7, 79]
print(average_temp(a_list))

a_list_2 = [5, 62, 72, 102]
print(average_temp(a_list_2))



