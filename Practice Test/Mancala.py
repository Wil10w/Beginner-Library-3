#The game Mancala is one of the oldest games in recorded
#history. You can read more about it here:
#https://www.thesprucecrafts.com/how-to-play-mancala-409424
#
#For this problem, though, you don't need to know how to
#play the game. All you need to know is the board layout
#and the conditions for winning.
#
#A Mancala board is made of two rows of 6 cups, with two
#bigger cups at the ends. Each cup holds some number of
#stones or chips. For our purposes, though, we'll include
#the bigger cups at the end of the corresponding rows.
#
#So, for us, a Mancala board is represented as a
#2-dimensional list of integers. Each item in the lists
#represents a cup, and the number represents how many
#stones are currently in that cup. For example, this
#could be one board:
#
# [[5, 3, 0, 2, 6, 8, 1],
#  [1, 6, 8, 0, 4, 1, 4]]
#
#With this board representation, the game is over when
#every cup is empty except the top left and the bottom
#right. When the game is over, whoever has more stones
#in their cup wins: if the top left has more stones, the
#top player wins. If the bottom right has more stones,
#the bottom player wins.
#
#Write a function called check_winner. check_winner takes
#as a 2-dimensional list representing a game board. You
#may assume list will always have two lists, each with
#7 items, corresponding to the board structure shown
#above.
#
#Your function should return one of four strings
#depending on the values of the list:
#
# - If the game is not over (that is, there are stones
#   in any bucket except for the top-left or bottom-
#   right), return "Keep playing!"
# - If the game is over and the top player wins (that is,
#   there are more stones in top-left than bottom-right),
#   return "Player 1 wins!"
# - If the game is over and the bottom player wins (that
#   is, there are more stones in the bottom-right than
#   the top-left), return "Player 2 wins!"
# - If the game is over but the score is tied (that is,
#   there is an equal number of stones in the top-left
#   and bottom-right), return "Draw!"


#Write your function here!
def check_winner(listOfLists):
    # a whole bunch of variables to keep track of game conditions
    #an a list for each player
    player1 = listOfLists[0]
    player2 = listOfLists[1]
    #this tells us how many of the lists indexes are at 0
    emptyScore1 = 0
    emptyScore2 = 0
    #this lets us know the players final scores, whether finished or not.
    # they are located at opposite ends of their lists - do index 0 and 6
    P1score = player1[0]
    P2score = player2[6]
    #this becomes True when all other indexes are at 0
    P1finished = False
    P2finished = False

    #looping over both list together using the zip() function
    for i, j in zip(player1, player2):

    #now we start scoring and checking
    #if i and j are equal to 0 - we plus 1 to EmptyScore 1 and 2
        if i == 0:
            emptyScore1 +=1
        if j == 0:
            emptyScore2 +=1
     #if either empty Scores are exual to 6 - which is the number of extra cups
    #it means the player has finished the game.
    if emptyScore1 == 6:
        P1finished = True
    if emptyScore2 == 6:
        P2finished = True

    # then we have the winning conditionals
    ###############################################
    #if one has all empty cups and the other doesn't
    if P1finished is True and P2finished is False:
        return "Player 1 wins!"
    if P1finished is False and P2finished is True:
        return "Player 2 wins!"
   ################################################
    #if both are finished
    if P1finished is True and P2finished is True:
        #we then need to check their P1 and P2 score
        if P1score > P2score:
            return "Player 1 wins!"
        elif P1score < P2score:
            return "Player 2 wins!"
    ################################################
   #if both have finished and both have the same score - Draw
    if P1finished is True and P2finished is True:
        if P1score == P2score:
            return "Draw!"
    ################################################
    #if neither have finished as True - keep playing
    if P1finished is False and P2finished is False:
        return 'Keep playing!'


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Keep playing!
#Player 1 wins!
#Player 2 wins!
#Draw!
keep_playing = [[5, 3, 0, 2, 6, 8, 1], [1, 6, 8, 0, 4, 1, 4]]
player1_wins = [[27, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 21]]
player2_wins = [[16, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 32]]
game_is_tied = [[24, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 24]]
print(check_winner(keep_playing))
print(check_winner(player1_wins))
print(check_winner(player2_wins))
print(check_winner(game_is_tied))

