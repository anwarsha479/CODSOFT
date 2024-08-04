import tkinter as tk
import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"
def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        message = f"It's a tie! Computer also chose {computer_choice}."
    elif result == "win":
        global user_score
        user_score += 1
        message = f"You win! Computer chose {computer_choice}."
    else:
        global computer_score
        computer_score += 1
        message = f"You lose! Computer chose {computer_choice}."

    result_label.config(text=message)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
    result_label.config(text="Choose rock, paper, or scissors!")
user_score = 0
computer_score = 0
root = tk.Tk()
root.title("Rock, Paper, Scissors")
top_frame = tk.Frame(root)
top_frame.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)
instruction_label = tk.Label(top_frame, text="Choose rock, paper, or scissors:")
instruction_label.pack()
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)
result_label = tk.Label(bottom_frame, text="Choose rock, paper, or scissors!")
result_label.pack()
score_label = tk.Label(bottom_frame, text=f"Score - You: {user_score} | Computer: {computer_score}")
score_label.pack()
reset_button = tk.Button(bottom_frame, text="Reset Game", command=reset_game)
reset_button.pack(pady=5)
root.mainloop()
