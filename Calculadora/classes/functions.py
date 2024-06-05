from tkinter import * # type: ignore
from tkinter import ttk


class Functions:

    def __init__(self) -> None:
        self.et_display: Entry

    def enter_mouse(self, event) -> None:
        event.widget.configure(bg="#505050")

    def leave_mouse(self, event) -> None:
        event.widget.configure(bg="#606060")

    def enter_mouse_orange(self, event) -> None:
        event.widget.configure(bg="#c95400")

    def leave_mouse_orange(self, event) -> None:
        event.widget.configure(bg="#fc6900")

    def not_focus_display(self, event, root) -> None:
        root.focus_force()
        
    def action(self, num: str) -> None:
        if num.isnumeric() or num in "+-x/,":
            self.__put_num_or_operator(num)
        elif num == "<-":
            self.__del_num()
        elif num == "C":
            self.__clean()
        elif num == "=":
            self.calculate()

    def __put_num_or_operator(self, num) -> None:
        if self.et_display["fg"] == "red":
            self.et_display["fg"] = "white"
        current_txt: str = self.et_display.get()
        if current_txt == "0 ":
            current_txt = ""
        num = str(num).replace(".", ",")
        self.et_display.delete(0, END)
        self.et_display.insert(0, current_txt.strip())
        self.et_display.insert(END, (num + " "))

    def __del_num(self) -> None:
        content = self.et_display.get()
        if len(content) == 2:
            self.et_display.delete(0, END)
            self.__put_num_or_operator(num=0)
        else:
            new_content = content[:-2]
            self.et_display.delete(0, END)
            self.__put_num_or_operator(num=new_content)

    def __clean(self) -> None:
        if self.et_display.get() == "0 ":
            pass
        else:
            self.et_display.delete(0, END)
            self.__put_num_or_operator(num=0)

    def __operation(self) -> str:
        operation: str = str(self.et_display.get())
        operation = operation.replace(",", ".")
        operation = operation.replace("x", "*")
        return operation

    def __invalid_operation(self) -> None:
        current_txt: str = self.et_display.get()
        self.et_display.delete(0, END)
        self.et_display["fg"] = "red"
        self.et_display.insert(0, current_txt)
        
    def calculate(self) -> None:
        operation: str = self.__operation()
        try:
            answer = float(eval(operation))
            self.et_display.delete(0, END)
            if answer.is_integer():
                answer = int(answer)
            self.__put_num_or_operator(num=answer)
        except SyntaxError:
            self.__invalid_operation()
        
    def key_press(self, event) -> None:
        if event.char in "0123456789/*-+,":
            self.__put_num_or_operator(num=event.char)
        elif event.char == "\x08":
            self.__del_num()
        elif event.char == "\r":
            self.calculate()

