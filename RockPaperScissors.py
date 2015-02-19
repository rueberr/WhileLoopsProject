#Rock Paper Scissors
#Created by Ryan Rueber


#import statements
import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
root = Tk()

def main():
    #create a window
    w = Label(root, text="Rock Paper Scissors")
    w.pack()

    # Variables


    #Welcome
    messagebox.showinfo("Hello!",
                        "This game will simulate a game " + \
                        "of rock paper scissors between you " + \
                        "and the computer. The first person " + \
                        "to score three points will win the game.")

    #While Loop
    computerwin = 0 #A sentinel variable
                  #keeps watch over while loop
    youwin = 0
    while computerwin < 3 and youwin < 3 :
        userchoice = simpledialog.askstring("User Choice", "Pick rock, paper, or scissors " + \
                                        "and type your choice. (Type 'stop' to quit the game).") #user input
        userchoice = userchoice.lower()
        computerchoice = random.randint(1,3) # rock paper or scissors
        if computerchoice == 1 and userchoice == "rock":
            messagebox.showinfo("Results", "Computer picked rock " + \
                                "and you picked rock. " + \
                                "It's a tie!")
        elif computerchoice == 2 and userchoice == "paper":
            messagebox.showinfo("Results", "Computer picked paper " + \
                                "and you picked paper. " + \
                                "It's a tie!")
        elif computerchoice == 3 and userchoice == "scissors":
            messagebox.showinfo("Results", "Computer picked scissors " + \
                                "and you picked scissors. " + \
                                "It's a tie!")
        elif computerchoice == 1 and userchoice == "scissors":
            messagebox.showinfo("Results", "Computer picked rock " + \
                                "and you picked scissors. " + \
                                "You lose! The computer gains " + \
                                "one point.")
            computerwin += 1
        elif computerchoice == 2 and userchoice == "rock":
            messagebox.showinfo("Results", "Computer picked paper " + \
                                "and you picked rock. " + \
                                "You lose! The computer gains " + \
                                "one point.")
            computerwin += 1
        elif computerchoice == 3 and userchoice == "paper":
            messagebox.showinfo("Results", "Computer picked scissors " + \
                                "and you picked paper. " + \
                                "You lose! The computer gains " + \
                                "one point.")
            computerwin += 1
        elif computerchoice == 3 and userchoice == "rock":
            messagebox.showinfo("Results", "Computer picked scissors " + \
                                "and you picked rock. " + \
                                "You win! You gain a point.")
            youwin += 1
        elif computerchoice == 2 and userchoice == "scissors":
            messagebox.showinfo("Results", "Computer picked paper " + \
                                "and you picked scissors. " + \
                                "You win! You gain a point.")
            youwin += 1
        elif computerchoice == 1 and userchoice == "paper":
            messagebox.showinfo("Results", "Computer picked rock " + \
                                "and you picked paper. " + \
                                "You win! You gain a point.")
            youwin += 1
        elif userchoice == "stop":
            messagebox.showinfo("Quit", "You have elected to quit " + \
                                "the game. Thanks for playing.")
            break
        else:
            messagebox.showinfo("Error", "Sorry but '{}' isn't a valid input. ".format(userchoice) + \
                                "Please try again.")

    if computerwin == 3:
        messagebox.showinfo ("Results", "The computer has three " + \
                             "points and you have lost the game.")
    if youwin == 3:
        messagebox.showinfo ("Results", "You have three " + \
                             "points and you have won the game.")

main()

play = "yes"
while play == "yes":
    play = simpledialog.askstring ("Play", "would you like to " + \
                                "play again? Type 'yes' or 'no'.")
    play = play.lower()
    if play == "yes":
        main()
    elif play == "no":
        root.destroy()
