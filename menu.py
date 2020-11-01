import curses


class Menu:
	def __init__(self, screen, items):
		self._screen = screen
		self._items = items
		self._selected = 0

	def display(self, internal=False):
		if not internal: # Internal calls to display shouldn't reset the screen and redraw the border
			self._screen.clear()
			self._screen.border()

		start_y, start_x = self._screen.getmaxyx()

		start_y = int((start_y / 2) - len(self._items))

		for item in self._items:
			attribute = 0

			if item == self._items[self._selected]:
				attribute |= curses.A_REVERSE

			self._screen.addstr(start_y, int((start_x / 2) - int(len(item) / 2)), item, attribute)
			start_y += 2

		return

	def selectItem(self):
		while True:
			key = self._screen.getch()
			screen_y, screen_x = curses.getsyx()

			if key == curses.KEY_UP:
				if(self._selected == 0):
					continue

				self._selected -= 1
				self.display(internal = True)
			elif key == curses.KEY_DOWN:
				if(self._selected == len(self._items) - 1):
					continue

				self._selected += 1
				self.display(internal = True)
			elif key == curses.KEY_ENTER or key == 10 or key == 13:
				return self._items[self._selected]

			self._screen.refresh()