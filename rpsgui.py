import random
import tkinter as tk
from tkinter import messagebox

def get_user_choice():
    """Get user's choice (Rock, Paper, or Scissors)"""
    return user_choice.get()

def get_computer_choice():
    """Generate computer's choice (Rock, Paper, or Scissors)"""
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game"""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose {user_choice}.")
    print(f"Computer chose {computer_choice}.\n")

    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", result)

def main():
    window = tk.Tk()
    window.title("Rock, Paper, Scissors")

    frame = tk.Frame(window)
    frame.pack()

    user_choice = tk.StringVar()
    user_choice.set("Rock")

    choice_label = tk.Label(frame, text="Enter your choice:")
    choice_label.pack()

    choice