import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'Computer wins!'

def on_button_click(user_choice):
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")

def create_game_ui():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")

    choices = ['rock', 'paper', 'scissors']

    for choice in choices:
        tk.Button(root, text=choice.capitalize(), padx=20, pady=20, command=lambda c=choice: on_button_click(c)).pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_game_ui()
