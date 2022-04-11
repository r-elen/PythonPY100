# tic-tac-toe
import tkinter as tk

first_player = 'X'
second_player = 'O'


def game_window():
    window = tk.Tk()  # создаем основное окно
    window.title("Крестики нолики")
    window.geometry('300x200')

    # frame = tk.Frame(root,)
    # but = tk.Button(root, text='Начать новую игру')
    # frame.pack()
    # but.pack(padx=5, pady=5)

    for i in range(3):
        for j in range(3):
            field_frame = tk.Frame(window, bd=1)
            field_frame.grid(row=i, column=j, padx=3, pady=3)
            label = tk.Button(field_frame, text=f"({i}, {j})")
            label.pack()

    window.mainloop()


def players_move():
    ...


def checking():
    ...


def game_moves():
    ...


if __name__ == '__main__':
    game_window()

