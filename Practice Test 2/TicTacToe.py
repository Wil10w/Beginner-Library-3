#In the game tic-tac-toe, two players take turns drawing
#Xs and Os on a 3x3 grid. If one player can place three of
#their symbols side-by-side in a row, column, or diagonal,
#they win the game.
#
#For example:
#
# X Wins:   X Wins:   X Wins:   No Winner:
# X|O|X     O|X|X     O|O|      X|O|O
# -+-+-     -+-+-     -+-+-     -+-+-
# O|O|X     X|O|      X|X|X     O|X|X
# -+-+-     -+-+-     -+-+-     -----
# O|X|X      | |O      | |      X|X|O
#
#Write a function called check_winner. check_winner will
#take one parameter as input, a 2D tuple (that is, a tuple
#of tuples). The 2D tuple represents the game board: each
#smaller tuple in the larger tuple is a row of the board,
#and each item in the smaller tuple is a spot on the
#board. There will always be three tuples in the larger
#tuple, and three items in each of the smaller tuples.
#
#Each item in the smaller tuple will always be one of three
#values: the string "X", the string "O", or the value None.
#
#check_winner should return one of three values: the string
#"X" if X has won the game; the string "O" if O has won the
#game; or the value None if there is no winner. None should
#NOT be the string "None"; it should be the value None,
#like the boolean values True and False.
#
#You may assume a player has won the game if and only if
#the board has three of their symbols in a row: you do not
#need to worry about whether the input is a valid game
#otherwise (e.g. a board of nine Xs still counts as X
#winning). You may assume that there will only be one
#winner per board.
#
#Hint: There are only eight possible places to win (three
#rows, three columns, two diagonals).


#Write your function here!
def check_winner(tupOfTups):
    #This is a simple yet long app. I basically checks for each winning variation through
    #the index of each letter in each tupple - using if statements

    #winning columns (x)
    if tupOfTups[0][0] == 'X' and tupOfTups[1][0] == 'X' and tupOfTups[2][0] == 'X':
        return 'X'
    if tupOfTups[0][1] == 'X' and tupOfTups[1][1] == 'X' and tupOfTups[2][1] == 'X':
        return 'X'
    if tupOfTups[0][2] == 'X' and tupOfTups[1][2] == 'X' and tupOfTups[2][2] == 'X':
        return 'X'

    #winning columns (O)
    if tupOfTups[0][0] == 'O' and tupOfTups[1][0] == 'O' and tupOfTups[2][0] == 'O':
        return 'O'
    if tupOfTups[0][1] == 'O' and tupOfTups[1][1] == 'O' and tupOfTups[2][1] == 'O':
        return 'O'
    if tupOfTups[0][2] == 'O' and tupOfTups[1][2] == 'O' and tupOfTups[2][2] == 'O':
        return 'O'

    #winning Diag (X)
    if tupOfTups[0][0] == 'X' and tupOfTups[1][1] == 'X' and tupOfTups[2][2] == 'X':
        return 'X'
    if tupOfTups[2][0] == 'X' and tupOfTups[1][1] == 'X' and tupOfTups[0][2] == 'X':
        return 'X'
    #winning diag (O)
    if tupOfTups[0][0] == 'O' and tupOfTups[1][1] == 'O' and tupOfTups[2][2] == 'O':
        return 'O'
    if tupOfTups[2][0] == 'O' and tupOfTups[1][1] == 'O' and tupOfTups[0][2] == 'O':
        return 'O'
    #this last one simplifies it even futher by checking each full tuple
    #winning rows
    if tupOfTups[0] == ('X', 'X', 'X',):
        return "X"
    if tupOfTups[0] == ('O', 'O', 'O'):
        return 'O'
    if tupOfTups[1] == ('X', 'X', 'X',):
        return  'X'
    if tupOfTups[1] == ('O', 'O', 'O'):
        return 'O'
    if tupOfTups[2] == ('X', 'X', 'X',):
        return 'X'
    if tupOfTups[2] == ('O', 'O', 'O'):
        return 'O'
    #if none of these statements are met, it just return None
    return None



#The code below shows how the tic-tac-toe tuples are
#created and tests your code with three games: one where
#X wins, one where O wins, and one where there is no winner.
#Remember, the line breaks in xwins and owins are optional:
#they're just to make the declarations more readable. They
#could be written the same as nowins.
xwins = (("X", "O", "X"),
         ("O", "O", ")"),
         ("X", "X", "X"))

owins = (("O", "X", "X"),
         ("X", "O", None),
         (None, None, "O"))

nowins = (("X", "O", "O"),
          ("O", "X", "X"),
          ("X", "X", "O"))
print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))


