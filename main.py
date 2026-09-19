import random
import tkinter

guessNumber = random.randint(1, 100)
attempts = 0
max_attempts = 7


def checkGuess():
    global attempts

    userGuess = int(guessEntry.get())
    guessEntry.delete(0, tkinter.END)
    attempts += 1

    attemptLbl.configure(text=f"Attempt {attempts} of {max_attempts}")

    if guessNumber > userGuess:
        resultLbl.configure(text="Your number is low", fg="orange")
    elif guessNumber < userGuess:
        resultLbl.configure(text="Your number is high", fg="red")
    else:
        resultLbl.configure(
            text=f"You guessed it in {attempts} attempts! Congrats!", fg="green"
        )
        guessBtn.configure(state=tkinter.DISABLED)

    if attempts == max_attempts and userGuess != guessNumber:
        resultLbl.configure(text=f"Game over! The number was {guessNumber}.", fg="red")
        guessBtn.configure(state=tkinter.DISABLED)


window = tkinter.Tk()
window.title("Guess the Number")
window.geometry("500x300")

titleLbl = tkinter.Label(
    window, text="Guess a number from 1 - 100", font=("Arial", 16, "bold")
)
titleLbl.place(x=100, y=30, width=300, height=30)

attemptLbl = tkinter.Label(window, text="Attempt 0 of 7", font=("Arial", 11))
attemptLbl.place(x=100, y=75, width=300, height=25)

guessEntry = tkinter.Entry(window, font=("Arial", 14), justify="center")
guessEntry.place(x=150, y=110, width=200, height=35)

guessBtn = tkinter.Button(
    window,
    text="Guess",
    fg="white",
    bg="green",
    font=("Arial", 11, "bold"),
    command=checkGuess,
)
guessBtn.place(x=200, y=160, width=100, height=35)

resultLbl = tkinter.Label(window, text="", font=("Arial", 11, "bold"))
resultLbl.place(x=50, y=220, width=400, height=30)

window.mainloop()
