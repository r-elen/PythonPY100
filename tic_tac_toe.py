# tic-tac-toe
import tkinter as tk

first_player = 'X'
second_player = 'O'


def game_window():
    root = tk.Tk()
    root.title("Крестики нолики")

    fra = tk.Frame(root, width=400, height=300)
    but = tk.Button(root, text='Начать новую игру')

    fra.pack()
    but.pack()
    root.mainloop()


def players_move():
    ...


def checking():
    ...


def game_moves():
    ...


if __name__ == '__main__':
    game_window()

