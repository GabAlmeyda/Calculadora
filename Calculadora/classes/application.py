from tkinter import * # type: ignore
from .functions import Functions

root = Tk()


class Application(Functions):

    def __init__(self) -> None:
        self.root = root
        self.screen()
        self.display_and_buttons()
        self.root.mainloop()

    def screen(self) -> None:
        self.root.title("Calculator")
        self.root.geometry("350x500+500+150")
        self.root.resizable(True, True)
        self.root.minsize(300, 400)
        self.root.configure(bg="#303030")

    def __frames(self) -> None:
        self.frame1 = Frame(self.root)
        self.frame1.configure(bg="#606060")
        self.frame1.place(relx=0.037, rely=0.025,
                          relwidth=0.935, relheight=0.2)

    def __buttons(self) -> None:
        buttons_num = ["7", "8", "9", "^",
                       "4", "5", "6", "/",
                       "1", "2", "3", "x",
                       ",", "0", "=", "-",
                       "C", "<-", "+"]

        relx = 0.035
        rely = 0.25
        relw = 0.2205
        relh = 0.13

        for pos, label in enumerate(buttons_num):
            button = Button(self.root, text=label, 
                            command=lambda num=label: self.action(num))
            if label == "C" or label == "<-": 
                relw = 0.33975
            if label == "+":
                relw = 0.2205
            #If the button is in the right side
            if label in ("+-x/^"):
                bg = "#fc6900" 
                activebackgroung = "#963f00" 
                button.bind("<Enter>", self.enter_mouse_orange)
                button.bind("<Leave>", self.leave_mouse_orange)
            else:
                bg = "#606060"
                activebackgroung = "#404040"
                button.bind("<Enter>", self.enter_mouse)
                button.bind("<Leave>", self.leave_mouse)
            button.configure(bg=bg, font=("verdana", 15, ("bold")),
                             activebackground=activebackgroung)
            button.place(relx=relx, rely=rely, relwidth=relw, relheight=relh)
            relx += 0.018 + relw
            if (pos + 1) % 4 == 0:
                relx = 0.035
                rely += 0.018 + relh

    def __display(self) -> None:
        self.et_display = Entry(self.frame1)
        self.et_display.configure(bg="#303030", font=(
            "arial", 30, ("bold", "italic")), fg="white", justify="right")
        self.et_display.bind("<FocusIn>", lambda event: self.not_focus_display(event, self.root))
        self.et_display.place(relx=0.014, rely=0.03,
                            relwidth=0.974, relheight=0.94)
        self.root.bind("<Any-KeyPress>", self.key_press) # type: ignore

    def display_and_buttons(self) -> None:
        self.__frames()
        self.__buttons()
        self.__display()


if __name__ == "__main__":
    Application()
    