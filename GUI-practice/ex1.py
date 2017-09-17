# Chen Hao
# GUI-practice, Fall 2016
# chen579@usc.edu

from tkinter import *

class GUI(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()

        self.__hintLabel = Label(self, text="Select your toppings")
        self.__hintLabel.grid(row=0, column=0, columnspan=3, sticky = "N")

        self.__value1 = BooleanVar()
        self.__value2 = BooleanVar()
        self.__value3 = BooleanVar()
        self.__value4 = StringVar()
        self.__radio1 = Checkbutton(self, variable = self.__value1, text="Pepperoni")
        self.__radio2 = Checkbutton(self, variable=self.__value2,  text="Sausage")
        self.__radio3 = Checkbutton(self, variable=self.__value3,  text="Extra Cheese")
        self.__radio4 = Radiobutton(self, variable = self.__value4, text="small", value = "small")
        self.__radio5 = Radiobutton(self, variable = self.__value4, text="medium", value = "medium")
        self.__radio6 = Radiobutton(self, variable = self.__value4, text="large", value = "large")

        self.__radio1.grid(row = 1, column = 0)
        self.__radio2.grid(row = 1, column = 1)
        self.__radio3.grid(row = 1, column = 2)
        self.__radio4.grid(row = 2, column = 0)
        self.__radio5.grid(row = 2, column = 1)
        self.__radio6.grid(row = 2, column = 2)

        self.__textbox = Text(self, width=80, height=10, bg="grey")
        self.__textbox.config(state="disabled")
        self.__textbox.grid(row=4, column=0, columnspan=3)

        self.__printButton = Button(self, text="Create order", command=self.displayOrder)
        self.__printButton.grid(row=3, column=0, columnspan=3)

    def displayOrder(self):
        output = ("Order: One "+str(self.__value4.get())+" pizza with")
        if self.__value1.get():
            output = output + " pepperoni"
        if self.__value2.get():
            output = output + " sausage"
        if self.__value3.get():
            output = output + " extra cheese"
        output = output+ "\n"
        self.__textbox.config(state="normal")
        self.__textbox.insert(END, output)
        self.__textbox.config(state="disabled")

def main():
    rootWindows = Tk()
    myApp = GUI(rootWindows)
    rootWindows.title("Pizza Orders")
    rootWindows.geometry("600x300")

    myApp.mainloop()

main()
