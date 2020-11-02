import curses

class Game:
	GAME_LIVE = 0
	GAME_OVER = 1

	_player = 0
	_player_symbols = ['X',	'O']

	def __init__(self, screen):
		self._screen = screen

	def initialise(self):
		rows, cols = self._screen.getmaxyx()
		board_visual = [
						'┏━━━━━━━┳━━━━━━━┳━━━━━━━┓',
						'┃       ┃       ┃       ┃',
						'┃       ┃       ┃       ┃',
						'┃       ┃       ┃       ┃',
						'┣━━━━━━━╋━━━━━━━╋━━━━━━━┫',
						'┃       ┃       ┃       ┃',
						'┃       ┃       ┃       ┃',
						'┃       ┃       ┃       ┃',
						'┣━━━━━━━╋━━━━━━━╋━━━━━━━┫',
						'┃       ┃       ┃       ┃',
						'┃       ┃       ┃       ┃',
						'┃       ┃       ┃       ┃',
						'┗━━━━━━━┻━━━━━━━┻━━━━━━━┛'
					]

		self._board = [
				[0, 0, 0],
				[0, 0, 0],
				[0, 0, 0]
			]
		self._board_x = 1
		self._board_y = 1
		self._quit = False

		self._screen.clear()
		self._screen.border()

		y = round((rows - len(board_visual)) / 2)
		x = round((cols - len(board_visual[0])) / 2)

		for row in board_visual:
			self._screen.addstr(y, x, row)
			y += 1

		y -= round(len(board_visual) / 2) + 1
		x += round(len(board_visual[0]) / 2)
		
		self._screen.move(y, x)
		self._screen.refresh()

	def takeTurn(self):
		while True:
			key = self._screen.getch()
			screen_y, screen_x = curses.getsyx()

			if key == curses.KEY_RIGHT:
				if(self._board_x == 2):
					continue

				self._board_x += 1
				self._screen.move(screen_y, screen_x + 8)
			elif key == curses.KEY_LEFT:
				if(self._board_x == 0):
					continue

				self._board_x -= 1
				self._screen.move(screen_y, screen_x - 8)
			elif key == curses.KEY_UP:
				if(self._board_y == 0):
					continue

				self._board_y -= 1
				self._screen.move(screen_y - 4, screen_x)
			elif key == curses.KEY_DOWN:
				if(self._board_y == 2):
					continue

				self._board_y += 1
				self._screen.move(screen_y + 4, screen_x)
			elif key == curses.KEY_ENTER or key == ord('\n') or key == ord('\r'):
				if self._board[self._board_y][self._board_x] != 0:
					continue

				self._screen.addstr(screen_y, screen_x, self._player_symbols[self._player])
				self._screen.move(screen_y, screen_x)
				self._board[self._board_y][self._board_x] = self._player_symbols[self._player]
				self._player = not self._player

				break
			elif key == ord('q'):
				self._quit = True

				break

			self._screen.refresh()

	def getState(self):
		if self._quit == True:
			return self.GAME_OVER

		for symbol in self._player_symbols:
			self._victor = self._player_symbols.index(symbol) + 1

			for i in range(0, 3):
				if self._board[i][0] == symbol and self._board[i][1] == symbol and self._board[i][2] == symbol:
					return self.GAME_OVER

			for i in range(0, 3):
				if self._board[0][i] == symbol and self._board[1][i] == symbol and self._board[2][i] == symbol:
					return self.GAME_OVER

			if self._board[0][0] == symbol and self._board[1][1] == symbol and self._board[2][2] == symbol:
				return self.GAME_OVER

			if self._board[2][0] == symbol and self._board[1][1] == symbol and self._board[0][2] == symbol:
				return self.GAME_OVER

		self._victor = 0

		if not any(0 in row for row in self._board):
			return self.GAME_OVER

		return self.GAME_LIVE

	def showVictor(self):
		if self._quit:
			self._quit = False
			return

		rows, cols = self._screen.getmaxyx()
		y = int(rows / 2)
		message = "It's a draw!"
		
		if self._victor:
			message = "Player " + str(self._victor) + " is victorious!"

		x = int(cols / 2) - int(len(message) / 2)

		self._screen.clear()
		self._screen.border()
		self._screen.addstr(y, x, message)
		self._screen.refresh()
		self._screen.getch()