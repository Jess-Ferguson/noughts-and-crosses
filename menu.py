import curses

class Menu:
	def __init__(self, screen, items, title = None):
		self._screen = screen
		self._title = title
		self._items = items
		self._selected = 0

	def display(self, internal=False):
		if not internal: # Internal calls to display shouldn't reset the screen and redraw the border
			self._screen.clear()
			self._screen.border()

		start_y, start_x = self._screen.getmaxyx()
		y = int(start_y / 2 - len(self._items))

		if self._title != None:
			x = int(start_x / 2 - len(self._title) / 2)

			self._screen.addstr(y - 3, x, self._title) # This will break if too many items are given

		for item in self._items:
			attribute = 0
			x = int(start_x / 2 - len(item) / 2)

			if item == self._items[self._selected]:
				attribute |= curses.A_REVERSE

			self._screen.addstr(y, x, item, attribute)

			y += 2

		self._screen.refresh()

	def selectItem(self):
		while True:
			key = self._screen.getch()
			screen_y, screen_x = curses.getsyx()

			if key == curses.KEY_UP:
				if(self._selected == 0):
					self._selected = len(self._items) - 1
				else:
					self._selected -= 1

				self.display(internal = True)
			elif key == curses.KEY_DOWN:
				if(self._selected == len(self._items) - 1):
					self._selected = 0
				else:
					self._selected += 1

				self.display(internal = True)
			elif key == curses.KEY_ENTER or key == ord('\n') or key == ord('\r'):
				return self._items[self._selected]

			self._screen.refresh()