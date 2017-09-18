from manage import manage

#save all of the points values in a dictionary
pointValues = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
               "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
               "y": 4, "z": 10}
def menu():  # display a menu
    print("1) Display points table and frequency table of 26 English letters")
    print("2) Display all two letter words")
    print("3) Show all 3 letters words containing a given tile")
    print("4) Verify your word in the dictionary")
    print("5) Show words that start with a \"Q\" but are not followed by a \"u\"")
    print("6) Show all the letters containing \"X\" or \"Z\" and a given tile")
    print("7) show all words that begin with given one or more letters.")
    print("8) show all words that end with given one or more letters.")
    print("9) Exit")

def main():
    dictlist = []
    f1 = manage("words.txt",dictlist)  # create an object of manage class (read file and save its every line into a list)
    print("Welcome to use Scrabble Helper.")

    while True:
        print()
        menu()
        choice = str(input("Please select your option:"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
            print("Invalid selection!")    #Error checking
            choice = int(input("Please select your option again:"))

        if choice == "1":
            f1.printTable()

        if choice == "2":
            twoletterlist = f1.twoLetters()  #use twoLetters function
            pointslist = []
            i = 0
            for item in twoletterlist:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(twoletterlist) - 1:
                print(twoletterlist[i] + " (points values:" + str(pointslist[i]) + ")")
                i += 1

        if choice == "3":
            letter = input("please enter the letter for the words:")
            threeletterlist = f1.inputLetter(letter.lower())   #use inputLetter function
            pointslist = []
            i = 0
            for item in threeletterlist:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(threeletterlist) - 1:
                print(threeletterlist[i] + " (points values:" + str(pointslist[i]) + ")")
                i += 1

        if choice == "4":
            word = input("please enter the word you want to check:")
            if f1.verifyExist(word.lower()):
                print("It exists within the Scrabble dictionary.\n")
            else:
                print("It doesn't exists within the Scrabble dictionary.\n")



        if choice == "5":
            qlist = f1.Qstart()  #use Qstart function
            pointslist = []
            i = 0
            for item in qlist:
                pointslist.append(f1.pointValue(item,pointValues))
                # print every word followed with its point value
            while i < len(qlist) - 1:
                print(qlist[i] + " (points values:" + str(pointslist[i]) + ")")
                i += 1


        elif choice == "6":
            checkletter = input("Please enter a letter:")
            xorzlist = f1.containXZ(checkletter.lower())  #use contain function
            pointslist = []
            i = 0
            for item in xorzlist:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(xorzlist) - 1:
                print(xorzlist[i] + " (points values:" + str(pointslist[i]) + ")")
                i += 1

        if choice == "7":
            tiles = input("Please enter a set of tiles:")
            beginList = f1.begin(tiles.lower())  # use begin function
            pointslist = []
            i = 0
            for item in beginList:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(beginList) - 1:
                print(beginList[i] + " (points values:" + str(pointslist[i]) + ")")
                i+=1

        if choice == "8":
            tiles = input("Please enter a set of tiles:")
            endList = f1.end(tiles.lower()) # use end function
            pointslist = []
            i = 0
            for item in endList:
                pointslist.append(f1.pointValue(item, pointValues))
                # print every word followed with its point value
            while i < len(endList) - 1:
                print(endList[i] + " (points values:" + str(pointslist[i]) + ")")
                i+=1

        if choice == "9":
            print("Goodbye.")
            break  #Exit

main()