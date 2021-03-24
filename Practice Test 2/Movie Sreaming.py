# Write a function called write_streaming_info.
# write_streaming_info will take as input two parameters: a
# string and a list.
#
# The string will represent the filename to which to write.
#
# Each item in the list will be a tuple. The first item of
# every tuple will be the name of a movie. All remaining items
# in the tuple will be streaming services on which the movie
# appears, such as Hulu, Netflix, Peacock, HBO Max, Amazon,
# Disney+, Peacock, YouTube, Crunchyroll, CBS All Access, etc.
#
# write_streaming_info should write the list of movies to the
# file given by the filename using the following format:
#
# [movie]: Available on Service_1, Service_2, and Service_3
#
# The movies and the streaming service names should appear in
# the order of the original list/tuples.
#
# So, for this list of tuples:
#
# [("Chocolat", "Hulu", "Netflix", "Amazon"),
#  ("Skyfall", "HBO Max", "Amazon"),
#  ("Soul", "Disney+")]
#
# The file printed would look like this:
#
# Chocolat: Available on Hulu, Netflix, and Amazon
# Skyfall: Available on HBO Max and Amazon
# Soul: Disney+
#
# Note that if only one service is listed, just that service
# appears after the colon. If two services are listed, they
# appear separated by 'and' with no commas. If three or more
# services are listed, then there is a comma after every
# service except the last one, and the last one is preceded
# by 'and'.

#
# HINT: Remember, you can use slicing on tuples just like strings.
# a_tuple[:2], for example, will give you the first two items in a
# tuple. a_tuple[3:] will give you all the items from the one at
# index 3 to the end.


# Write your function here!
def write_streaming_info(afile, listOfTups):

    finalString = ''
    outputfile = open(afile, 'a')

    for tup in listOfTups:
        finalString = tup[0] + ': '

        for i in range(1, len(tup) - 1):
            finalString = finalString + tup[i] + ', '
        finalString = finalString.rstrip(', ')

        if len(tup) == 3:
            finalString = finalString + ' and ' + tup[len(tup)-1]
        if len(tup) > 3:
            finalString = finalString + ', and ' + tup[len(tup) - 1]


        if len(tup) < 3:
            finalString = finalString + ' ' + tup[len(tup) - 1]
        finalString = finalString.strip()
        print(finalString, file=outputfile)




# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print nothing -- however, it should write the same contents
# as Sample.txt to Test.txt.
movies = [("Chocolat", "Hulu", "Netflix", "Amazon"), ("Skyfall", "HBO Max", "Amazon"), ("Soul", "Disney+")]
write_streaming_info("Test.txt", movies)



