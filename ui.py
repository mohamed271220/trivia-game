from tkinter import *

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("quiz app")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.my_label = Label(text="score:", fg="white", bg=THEME_COLOR)
        self.my_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quest_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                  font=("Arial", 25, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img= PhotoImage(file="images/true.png")
        self.true_button= Button(image=true_img, highlightthickness=0)
        self.true_button.grid(row=2,column=1)
        false_img= PhotoImage(file="images/false.png")
        self.false_button= Button(image=false_img, highlightthickness=0)
        self.false_button.grid(row=2,column=0)
        self.window.mainloop()
