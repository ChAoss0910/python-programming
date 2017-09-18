from tkinter import *

from manage_gui import manage

class GUI(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()

        self.__hintLabel = Label(self, text="Welcome to Scrabble Helper!")
        self.__hintLabel.grid(row=0, column=0, columnspan=3, sticky = "N")

        self.__value = StringVar()
        self.__radio1 = Radiobutton(self, variable=self.__value, text="Display points table and frequency table of 26 English letters", value="1")
        self.__radio2 = Radiobutton(self, variable=self.__value, text="Display all two letter words",value="2")
        self.__radio3 = Radiobutton(self, variable=self.__value, text="Show all 3 letters words containing a given tile",value="3")
        self.__radio4 = Radiobutton(self, variable=self.__value, text="Verify your word in the dictionary",value="4")
        self.__radio5 = Radiobutton(self, variable=self.__value, text="Show words that start with a \"Q\" but are not followed by a \"u\"",value="5")
        self.__radio6 = Radiobutton(self, variable=self.__value, text="Show all the letters containing \"X\" or \"Z\" and a given tile",value="6")
        self.__radio7 = Radiobutton(self, variable=self.__value, text="Show all words that begin with given one or more letters.",value="7")
        self.__radio8 = Radiobutton(self, variable=self.__value, text="Show all words that end with given one or more letters.",value="8")

        self.__radio1.grid(row=1, column=0,sticky = "W")
        self.__radio2.grid(row=2, column=0,sticky = "W")
        self.__radio3.grid(row=3, column=0,sticky = "W")
        self.__radio4.grid(row=4, column=0,sticky = "W")
        self.__radio5.grid(row=5, column=0,sticky = "W")
        self.__radio6.grid(row=6, column=0,sticky = "W")
        self.__radio7.grid(row=7, column=0,sticky = "W")
        self.__radio8.grid(row=8, column=0,sticky = "W")

        self.__printButton = Button(self, text="Submit", command=self.displayOrder)
        self.__printButton.grid(row=11, column=0, columnspan=3)

        self.__entrybox = Entry(self, bd = 2.5)
        self.__entrybox.grid(row=10, column=0, columnspan=3)

        self.__textbox = Text(self, width=80, height=20, bg="grey")
        self.__textbox.config(state="disabled")
        self.__textbox.grid(row=12, column=0, columnspan=3,sticky ="N")

        self.__printButton = Button(self, text="Clear", command=self.cleartext)
        self.__printButton.grid(row=33, column=0, columnspan=3,sticky = "E")

    def cleartext(self):
        self.__textbox.delete(0.0,END)
        self.__textbox.config(state="disabled")

    def displayOrder(self):
        pointValues = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                       "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                       "y": 4, "z": 10}
        output = ""
        dictlist = []
        f1 = manage("words.txt", dictlist)
        if self.__value.get() == "1":
            output = f1.printTable()
        if self.__value.get() == "2":
            twoletterlist = f1.twoLetters()  # use twoLetters function
            pointslist = []
            i = 0
            for item in twoletterlist:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(twoletterlist) - 1:
                output += twoletterlist[i] + " (points values:" + str(pointslist[i]) + ")" + "\n"
                i += 1
        if self.__value.get()=="3":
            letter = str(self.__entrybox.get())
            threeletterlist = f1.inputLetter(letter.lower())  # use inputLetter function
            pointslist = []
            i = 0
            for item in threeletterlist:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(threeletterlist) - 1:
                output += threeletterlist[i] + " (points values:" + str(pointslist[i]) + ")" + "\n"
                i += 1
        if self.__value.get()=="4":
            word = str(self.__entrybox.get())
            if f1.verifyExist(word.lower()):
                output = "It exists within the Scrabble dictionary.\n"
            else:
                output = "It doesn't exists within the Scrabble dictionary.\n"

        if self.__value.get()=="5":
            qlist = f1.Qstart()  # use Qstart function
            pointslist = []
            i = 0
            for item in qlist:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(qlist) - 1:
                output += qlist[i] + " (points values:" + str(pointslist[i]) + ")"+"\n"
                i += 1
        if self.__value.get()=="6":
            checkletter = str(self.__entrybox.get())
            xorzlist = f1.containXZ(checkletter.lower())  # use contain function
            pointslist = []
            i = 0
            for item in xorzlist:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(xorzlist) - 1:
                output += xorzlist[i] + " (points values:" + str(pointslist[i]) + ")"+"\n"
                i += 1
        if self.__value.get()=="7":
            tiles = str(self.__entrybox.get())
            beginList = f1.begin(tiles.lower())  # use begin function
            pointslist = []
            i = 0
            for item in beginList:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(beginList) - 1:
                output += beginList[i] + " (points values:" + str(pointslist[i]) + ")"+ "\n"
                i += 1
        if self.__value.get()=="8":
            tiles = str(self.__entrybox.get())
            endList = f1.end(tiles.lower())  # use end function
            pointslist = []
            i = 0
            for item in endList:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(endList) - 1:
                output += endList[i] + " (points values:" + str(pointslist[i]) + ")"+"\n"
                i += 1

        output = output + "\n"+"\n"
        self.__textbox.config(state="normal")
        self.__textbox.insert(END, output)
        #self.__textbox.config(state="disabled")

def main():
    rootWindows = Tk()
    myApp = GUI(rootWindows)
    rootWindows.title("Scrabble Helper")
    rootWindows.geometry("570x650")

    myApp.mainloop()

main()