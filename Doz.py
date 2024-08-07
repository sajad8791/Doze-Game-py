import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.window = tk.Tk()
        self.window.title('بازی دوز')
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.create_board_buttons()

    def create_board_buttons(self):
        self.buttons = [[tk.Button(self.window, text='', font=('', 34), width=10, height=3,
                                   command=lambda row=row, col=col: self.make_move(row, col)) for col in range(self.board_size)]
                                   for row in range(self.board_size)]    
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f" برنده شد {self.current_player} بازی کن")
                self.reset_game()
            elif self.is_full():
                messagebox.showinfo("بازی شما مساوی شد")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            messagebox.showerror("خانه پر است خانه دیگری انتخاب کنید ")  
           
    def check_win(self, player):      
        for i in range(self.board_size):
            if all(self.board[i][j] == player for j in range(self.board_size)) or all(self.board[j][i] == player for j in range(self.board_size)):
                return True
        return all(self.board[i][i] == player for i in range(self.board_size)) or all(self.board[i][self.board_size - 1 - i] == player for i in range(self.board_size))


    def is_full(self):
        return all(all(cell != ' ' for cell in row)for row in self.board)
    
    def reset_game(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.board[row][col]= ' '
                self.buttons[row][col].config(text=' ')
        self.current_player = 'X'        

    def run(self):
        self.window.mainloop()     

if __name__ == "__main__":
    board_size = int(input("Enter the size of board : "))
    tic_tac_toe = TicTacToeGUI(board_size)
    tic_tac_toe.run()     