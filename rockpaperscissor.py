import tkinter as tk
import random

# Initialize main application window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="black")
root.geometry("600x400")

# Game variables
choices = ["✊", "✋", "✌"]
player_score = 0
computer_score = 0
winning_score = 3

# Functions
def play_game(player_choice):
    global player_score, computer_score

    # Clear previous PC button highlights
    reset_pc_button_highlights()

    # Determine computer's choice
    computer_choice = random.choice(choices)

    # Highlight the computer's choice
    for btn, choice in zip(pc_buttons, choices):
        if choice == computer_choice:
            btn.config(bg="yellow")

    # Determine the winner for this round
    if player_choice == computer_choice:
        result_text = "It's a tie!"
    elif (player_choice == "✊" and computer_choice == "✌") or \
         (player_choice == "✋" and computer_choice == "✊") or \
         (player_choice == "✌" and computer_choice == "✋"):
        result_text = "You win this round!"
        player_score += 1
    else:
        result_text = "Computer wins this round!"
        computer_score += 1

    # Update scores and result
    player_score_label.config(text=f"You: {player_score}")
    computer_score_label.config(text=f"PC: {computer_score}")
    result_label.config(text=result_text)

    reset_pc_button_highlights()

    # Check if someone reached the winning score
    if player_score == winning_score or computer_score == winning_score:
        declare_winner()

def reset_pc_button_highlights():
    """Clear the background of all PC buttons."""
    for btn in pc_buttons:
        btn.config(bg=None)  # Reset to default background

def declare_winner():
    global player_score, computer_score

    # Determine final winner
    if player_score == winning_score:
        final_result = "Congratulations! You win the game!"
    else:
        final_result = "Computer wins the game! Better luck next time!"

    # Display final result and disable buttons
    result_label.config(text=final_result)
    for btn in player_buttons:
        btn.config(state="disabled")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0

    # Reset UI
    player_score_label.config(text="You: 0")
    computer_score_label.config(text="PC: 0")
    result_label.config(text="")

    # Clear PC button highlights
    reset_pc_button_highlights()

    # Enable player buttons
    for btn in player_buttons:
        btn.config(state="normal")

def disable_buttons():
    # Disable player buttons initially
    for btn in player_buttons:
        btn.config(state="disabled")

# Header
header = tk.Frame(root, bg="black")
header.pack(pady=10)

title_label = tk.Label(header, text="Rock Paper Scissors", font=("Arial", 24), bg="black", fg="yellow")
title_label.pack()

score_container = tk.Frame(header, bg="black")
score_container.pack(pady=10)

tk.Label(score_container, text="Score", font=("Arial", 16), bg="black", fg="yellow").pack()
player_score_label = tk.Label(score_container, text="You: 0", font=("Arial", 14), bg="black", fg="yellow")
player_score_label.pack(side=tk.LEFT, padx=20)
computer_score_label = tk.Label(score_container, text="PC: 0", font=("Arial", 14), bg="black", fg="yellow")
computer_score_label.pack(side=tk.RIGHT, padx=20)

# Main content
main_content = tk.Frame(root, bg="black")
main_content.pack(pady=10, fill="both", expand=True)

# Player section
player_container = tk.Frame(main_content, bg="#44ff00", highlightbackground="#765858", highlightthickness=3)
player_container.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

player_label = tk.Label(player_container, text="You", font=("Arial", 18), bg="#44ff00", fg="black")
player_label.pack(pady=10)

player_buttons = []
for choice in choices:
    btn = tk.Button(player_container, text=choice, font=("Arial", 18), command=lambda c=choice: play_game(c))
    btn.pack(pady=5)
    player_buttons.append(btn)

# Disable buttons initially
disable_buttons()

# Computer section
pc_container = tk.Frame(main_content, bg="#9042d8", highlightbackground="#765858", highlightthickness=3)
pc_container.pack(side=tk.RIGHT, fill="both", expand=True, padx=10, pady=10)

pc_label = tk.Label(pc_container, text="PC", font=("Arial", 18), bg="#9042d8", fg="white")
pc_label.pack(pady=10)

pc_buttons = []
for choice in choices:
    btn = tk.Button(pc_container, text=choice, font=("Arial", 18), state="disabled")
    btn.pack(pady=5)
    pc_buttons.append(btn)

# Footer
footer = tk.Frame(root, bg="black")
footer.pack(pady=10)

result_label = tk.Label(footer, text="", font=("Arial", 16), bg="black", fg="yellow")
result_label.pack(pady=10)

start_button = tk.Button(footer, text="Start Game", font=("Arial", 14), bg="#395adf", fg="white", command=reset_game)
start_button.pack(pady=10)

# Run the application
root.mainloop()
