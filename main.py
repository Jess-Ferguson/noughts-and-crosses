import curses
from curses import wrapper

class Game:
	def __init__(self, screen):
		self._screen = screen

	def init_board(self):
		rows, cols = self._screen.getmaxyx()
		y = int((rows / 2) - 7)
		x = int((cols / 2) - 12)

		self._screen.addstr(y, x + 0, '┏━━━━━━━┳━━━━━━━┳━━━━━━━┓')
		self._screen.addstr(y + 1, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 2, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 3, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 4, x, '┣━━━━━━━╋━━━━━━━╋━━━━━━━┫')
		self._screen.addstr(y + 5, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 6, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 7, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 8, x, '┣━━━━━━━╋━━━━━━━╋━━━━━━━┫')
		self._screen.addstr(y + 9, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 10, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 11, x, '┃       ┃       ┃       ┃')
		self._screen.addstr(y + 12, x, '┗━━━━━━━┻━━━━━━━┻━━━━━━━┛')

		self._screen.move(int(rows / 2) - 1, int(cols / 2))

	def loop(self): # This is more or less what a game turn will look like, the actual loop will be in the main() function
					# Should internally keep track of whose turn it is
		board_x = 1
		board_y = 1

		while True:
			key = self._screen.getch()
			screen_y, screen_x = curses.getsyx()
			
			if key == curses.KEY_RIGHT:
				if(board_x == 2):
					continue

				board_x += 1

				self._screen.move(screen_y, screen_x + 8)
			elif key == curses.KEY_LEFT:
				if(board_x == 0):
					continue

				board_x -= 1

				self._screen.move(screen_y, screen_x - 8)
			elif key == curses.KEY_UP:
				if(board_y == 0):
					continue

				board_y -= 1

				self._screen.move(screen_y - 4, screen_x)
			elif key == curses.KEY_DOWN:
				if(board_y == 2):
					continue

				board_y += 1
				
				self._screen.move(screen_y + 4, screen_x)
			elif key == ord('q'):
				break

			self._screen.refresh()


class Menu:
	def __init__(self, screen, items):
		self._screen = screen
		self._items = items

	def loop(self):
		return


def main(stdscr):
	stdscr.keypad(True)
	stdscr.clear()

	# Show menu screen

	menu = Menu(stdscr, 3)

	# menu.draw()

	stdscr.border()

	rows, cols = stdscr.getmaxyx()

	game = Game(stdscr)

	game.init_board()
	game.loop()

	# while game.getState() not game.GAME_OVER:
	#	game.takeTurn()

	key = stdscr.getkey()

wrapper(main)