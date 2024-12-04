import random
from tkinter import *

def play(choice):
    user_choice.set(choice)
    comp_choice.set(random.choice(["Rock", "Paper", "Scissors"]))
    if user_choice.get() == comp_choice.get():
        result.set("It's a Tie!")
    elif (user_choice.get() == "Rock" and comp_choice.get() == "Scissors") or \
         (user_choice.get() == "Scissors" and comp_choice.get() == "Paper") or \
         (user_choice.get() == "Paper" and comp_choice.get() == "Rock"):
        result.set("You Win!")
    else:
        result.set("You Lose!")

root = Tk()
root.title("Rock Paper Scissors")

user_choice = StringVar()
comp_choice = StringVar()
result = StringVar()

Label(root, text="Rock Paper Scissors Game", font=("Arial", 16)).pack(pady=10)
Button(root, text="Rock", font=("Arial", 14), command=lambda: play("Rock")).pack(pady=5)
Button(root, text="Paper", font=("Arial", 14), command=lambda: play("Paper")).pack(pady=5)
Button(root, text="Scissors", font=("Arial", 14), command=lambda: play("Scissors")).pack(pady=5)

Label(root, text="Your Choice:", font=("Arial", 12)).pack(pady=5)
Label(root, textvariable=user_choice, font=("Arial", 12)).pack()

Label(root, text="Computer's Choice:", font=("Arial", 12)).pack(pady=5)
Label(root, textvariable=comp_choice, font=("Arial", 12)).pack()

Label(root, text="Result:", font=("Arial", 12)).pack(pady=5)
Label(root, textvariable=result, font=("Arial", 12, "bold")).pack()

root.mainloop()
