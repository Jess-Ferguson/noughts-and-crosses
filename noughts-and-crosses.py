#!/usr/bin/python3

import curses
from menu import Menu
from game import Game

def main(stdscr):
	stdscr.keypad(True)

	menu = Menu(stdscr, [ "One Player", "Two Player", "Zero Players", "Quit" ], title = "Noughts and Crosses v0.1")

	while True:
		menu.display()

		choice = menu.selectItem()

		if choice == "One Player":
			# TODO: Implement AI single player mode
			continue
		elif choice == "Two Player":
			game = Game(stdscr)

			game.initialise()

			while game.getState() != game.GAME_OVER:
				game.takeTurn()

			game.showVictor()
		elif choice == "Zero Players":
			# TODO: Make the AI play itself
			# TODO: If chosen 10 times in a row, display the ending message from WarGames
			continue
		elif choice == "Quit":
			break


curses.wrapper(main)

print("Thanks for playing!")
