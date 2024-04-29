import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memory Game")
        self.geometry("300x300")
        self.cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 2
        random.shuffle(self.cards)
        self.attempts = 0
        self.first_card = None
        self.second_card = None

        self.create_board()

    def create_board(self):
        self.buttons = []
        for i in range(4):
            for j in range(5):
                button = tk.Button(self, text=" ", width=4, height=2, command=lambda row=i, col=j: self.card_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

    def card_click(self, row, col):
        index = 5 * row + col
        card = self.cards[index]
        self.buttons[index].config(text=str(card))

        if self.first_card is None:
            self.first_card = (row, col)
        else:
            self.second_card = (row, col)
            self.after(1000, self.check_match)

    def check_match(self):
        row1, col1 = self.first_card
        row2, col2 = self.second_card

        index1 = 5 * row1 + col1
        index2 = 5 * row2 + col2

        if self.cards[index1] == self.cards[index2]:
            self.buttons[index1].config(state="disabled")
            self.buttons[index2].config(state="disabled")
            self.attempts += 1
            if self.attempts == 10:
                messagebox.showinfo("Congratulations!", f"You completed the game with {self.attempts} attempts!")
                self.destroy()
        else:
            self.buttons[index1].config(text=" ")
            self.buttons[index2].config(text=" ")

        self.first_card = None
        self.second_card = None

def main():
    game = MemoryGame()
    game.mainloop()

if __name__ == "__main__":
    main()
