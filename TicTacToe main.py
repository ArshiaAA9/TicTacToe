import tkinter as tk


class Board:
    def __init__(self, root):
        self.root = root
        self.root.title("TicTacToe Deluxe")
        icon_path = "Icon.ico"
        self.root.iconbitmap(icon_path)
        self.root.geometry('250x350')
        self.root.config(bg='black')

        self.button_frame = tk.Frame(self.root, pady=3, bg='black')  # make frame for our buttons
        self.button_frame.pack(side='bottom')

        self.current_player = "X"

        self.show_current_player = tk.Label(self.root,
                                            text=f'{self.current_player} to move',
                                            font=("Comic Sans MS", 14),
                                            bg='cyan',
                                            borderwidth=1,
                                            relief='solid',
                                            pady=3,
                                            padx=15)
        self.show_current_player.pack(side='top')

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

        self.reset_button = tk.Button(self.root, text='Reset Game',
                                      font=("Comic Sans MS", 11),
                                      borderwidth=2,
                                      relief="solid",
                                      command=self.reset_game)
        self.reset_button.pack(side='bottom')

        self.move_counter = 0

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.button_frame,
                                   text="",
                                   width=10,
                                   height=5,
                                   pady=1,
                                   bg='magenta',
                                   command=lambda r=row, c=col: self.on_button_click(r, c),)
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        button = self.buttons[row][col]
        if button.cget("text") == "":
            if self.current_player == 'X':
                button.config(text="X", bg='cyan')
                self.current_player = "O"
                self.show_current_player.config(text=f'{self.current_player} to move', bg='yellow')
            else:
                button.config(text='O', bg='yellow')
                self.current_player = "X"
                self.show_current_player.config(text=f'{self.current_player} to move', bg='cyan')
            self.move_counter += 1
            if self.move_counter >= 5:
                if self.check_winner():
                    if self.current_player == "X":
                        self.current_player = "O"
                        self.show_current_player.config(bg='yellow')
                    else:
                        self.current_player = "X"
                        self.show_current_player.config(bg='cyan')
                    self.show_current_player.config(text=f'player {self.current_player} has Won!')
            if self.move_counter > 8:
                self.show_current_player.config(text='No one has Won')

        else:
            self.show_current_player.config(text=f'invalid housing {self.current_player} to move ')

    def check_winner(self):
        # Check Rows
        for row in range(3):
            if self.buttons[row][0].cget("text") == self.buttons[row][1].cget("text") == self.buttons[row][2].cget(
                    "text") and self.buttons[row][0].cget("text") != "":
                return True

        # Check Columns
        for col in range(3):
            if self.buttons[0][col].cget("text") == self.buttons[1][col].cget("text") == self.buttons[2][col].cget(
                    "text") and self.buttons[0][col].cget("text") != "":
                return True

        # Check Diagonal
        if self.buttons[0][0].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][2].cget("text") and \
                self.buttons[0][0].cget("text") != "":
            return True

        # Check Diagonal
        if self.buttons[0][2].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][0].cget("text") and \
                self.buttons[0][2].cget("text") != "":
            return True

        return False

    def reset_game(self):
        self.move_counter = 0
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')
                self.buttons[row][col].config(bg='magenta')


if __name__ == '__main__':
    main_window = tk.Tk()
    game = Board(main_window)
    main_window.mainloop()
