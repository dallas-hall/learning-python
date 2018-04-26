def printGameBoard():
	print(game_board['Top Left'] + "|" + game_board['Top Middle'] + "|" + game_board['Top Right'])
	print('-+-+-')
	print(game_board['Middle Left'] + "|" + game_board['Middle Middle'] + "|" + game_board['Middle Right'])
	print('-+-+-')
	print(game_board['Bottom Left'] + "|" + game_board['Bottom Middle'] + "|" + game_board['Bottom Right'])

game_board = {
	'Top Left':' ', 'Top Middle': ' ', 'Top Right': ' '
	,'Middle Left': ' ', 'Middle Middle': ' ', 'Middle Right': ' '
	,'Bottom Left': ' ', 'Bottom Middle': ' ', 'Bottom Right': ' '
}

turn = 'X'
printGameBoard()
for i in range(9):
	print('It is ' + turn + "'s turn. Where do they want to move? E.g. Top Left, Bottom Middle, Middle Right")
	move = input()
	print(move)
	game_board[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
	printGameBoard()





