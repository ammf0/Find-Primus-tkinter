import os, sys
import random
try:
	from playsound import playsound
	from tkinter import messagebox
	import tkinter as tk
except:
	print("Oops!", sys.exc_info()[0], "occured!")
	print("Please make sure you have installed all required libraries!")
	sys.exit()


class Primus(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title("Flappy Primus")
		self.resizable(0,0)

		self.p, self.q, self.t = 0,0,0
		self.primes = [
			2, 3, 5, 7, 11,
			13, 17, 19, 23, 29,
			31, 37, 41, 43, 47,
			53, 59, 61, 67, 71,
			73, 79, 83, 89, 97,
			101, 103, 107, 109, 113,
			127, 131, 137, 139, 149,
			151, 157, 163, 167, 173,
			179, 181, 191, 193, 197,
			199, 211, 223, 227, 229,
			233, 239, 241, 251, 257,
			263, 269, 271, 277, 281,
			283, 293, 307, 311, 313,
			317, 331, 337, 347, 349,
			353, 359, 367, 373, 379,
			383, 389, 397, 401, 409,
			419, 421, 431, 433, 439,
			443, 449, 457, 461, 463,
			467, 479, 487, 491, 499
		]
		self.font_style = {
			'head' 			: 'Helvatica 12 bold',
			'config_button' : 'Helvatica 10',
			'game_timer'	: 'Helvatica 14 italic',
			'game_button' 	: 'Helvatica 9',
			'game_board'	: 'Helvatica 10 italic'
		}

		# ========== MAIN GAME ==========
		
		self.primus_head = tk.Label(self, text="Find All the Prime Numbers!".upper(),
			font = self.font_style['head'])
		self.primus_head.grid(row=0, column=0, columnspan=10)
		
		self.count = tk.Label(self, font = self.font_style['game_board'])
		self.count.grid(row=1, columnspan=6)
		self.count_number = 60
		self.countdown()

		self.game_button = [i for i in range(30)]

		for i in range(len(self.game_button)):
			self.create_number = random.randint(0,500)
			if (self.create_number in self.primes):
				self.t += 1

			# Do not change the <command> to using lambda
			# It just pass the last i and create_number

			self.game_button[i] = tk.Button(self, text = self.create_number, font = self.font_style['game_button'],
				padx=5, width=8, height=4, disabledforeground='black', command = self.check_ans(i, self.create_number))
			xrow,xcol = divmod(i,6)
			xrow+=3
			self.game_button[i].grid(row=xrow, column=xcol)

		# ========== SCORE BOARD ==========

		tk.Label(self, text='').grid(row=8)
		self.correct_ans = tk.Label(self, text="Correct\nAnswer", font = self.font_style['config_button'])
		self.correct_board = tk.Entry(self, width=5, state='disabled', font = self.font_style['game_board'],
			disabledforeground='black')
		self.wrong_ans = tk.Label(self, text="Wrong\nAnswer", font = self.font_style['config_button'])
		self.wrong_board = tk.Entry(self, width=5, state='disabled', font = self.font_style['game_board'],
			disabledforeground='black')

		self.correct_ans.grid(row=9, column=1)
		self.correct_board.grid(row=9, column=2)
		self.wrong_ans.grid(row=9, column=3)
		self.wrong_board.grid(row=9, column=4)

		# ========== QUIT AND RESTART ==========

		tk.Label(self, text='').grid(row=10)
		self.quit_game = tk.Button(self, text='Quit\nGame', font = self.font_style['config_button'],
			padx=5, width=8, command=self.quit_g)
		self.restart_game = tk.Button(self, text='Restart\nGame', font = self.font_style['config_button'],
			padx=5, width=8, command=self.restart_g)
		self.quit_game.grid(row=11, column=2)
		self.restart_game.grid(row=11, column=3)
		
		tk.Label(self, text='').grid(row=12)

	def check_ans(self, i, number):
		"""" Check the number in the game_button, is it a Prime or Not """
		def _check_ans():
			if (number in self.primes):
				playsound('sounds/correct.mp3')
				self.p += 1
				self.correct_board.configure(state='normal')
				self.correct_board.delete(0, tk.END)
				self.correct_board.insert(0, str(self.p))
				self.correct_board.configure(state='disabled')
				self.game_button[i].configure(bg='#90EE90')
				if (self.p == self.t):
					self.countdown_cancel()
					messagebox.showinfo("All Done", "Great! You've Found All the Prime Numbers!")
			else:
				playsound('sounds/wrong.mp3')
				self.q += 1
				self.wrong_board.configure(state='normal')
				self.wrong_board.delete(0, tk.END)
				self.wrong_board.insert(0, str(self.q))
				self.wrong_board.configure(state='disabled')
				self.game_button[i].configure(bg='#FF0000')

			self.game_button[i].configure(state='disabled')
		
		# Because lambda did not work, check_ans designed to return a method: _check_ans()
		return _check_ans

	def countdown(self):
		""" Game Timer """
		self.count_number -= 1
		self.count.configure(text=str(self.count_number))
		if (self.count_number > 0):
			self.after(1000, self.countdown)
		else:
			self.count.configure(text='0', state='disabled')
			for button in self.game_button:
				button.configure(state='disabled')

	def countdown_cancel(self):
		""" Game Timer Stopper. Executed when all Prime Numbers had been found"""
		if (self.count_number is not None):
			self.count.configure(text='0')
			self.after_cancel(self.count_number)
			self.count_number = 0

	def quit_g(self):
		if (messagebox.askyesno("Quit Game", "Are You Sure?")):
			self.quit()

	def restart_g(self):
		if (messagebox.askyesno("Restart Game", "Are You Sure?")):
			python = sys.executable
			os.execl(python, python, * sys.argv)


# ========== MAIN PROGRAM ==========

if (__name__ == '__main__'):
	primus = Primus()
	primus.mainloop()
