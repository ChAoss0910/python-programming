
class manage(object):

    def __init__(self,filename,dictionary):  #filename and dictionary are instance attributes.
        fileIn = open(filename, "r")  # open file
        for line in fileIn:
            line=line.strip()
            dictionary.append(line)
        self.__dictionary=dictionary

    def printTable(self):   # feature1: display Scrabble points values and frequencies for all 26 letters of English
        msg = "A is worth 1 - " + "a's frequency is 8.167%\n" + "B is worth 3 - " + "b's frequency is 1.492%\n" + \
              "C is worth 3 - " + "c's frequency is 2.782%\n" + "D is worth 2 - " + "d's frequency is 4.253%\n" + \
              "E is worth 1 - " + "e's frequency is 12.702%\n" + \
              "F is worth 4 - " + "f's frequency is 2.228%\n" + "G is worth 2 - " + "g's frequency is 2.015%\n" + \
              "H is worth 4 - " + "h's frequency is 6.094%\n" + "I is worth 1 - " + "i's frequency is 6.966%\n" + \
              "J is worth 8 - " + "j's frequency is 0.153%\n" + "K is worth 5 - " + "k's frequency is 0.772%\n" + \
              "L is worth 1 - " + "l's frequency is 4.025%\n" + "M is worth 3 - " + "m's frequency is 2.406%\n" + \
              "N is worth 1 - " + "n's frequency is 6.749%\n" + "O is worth 1 - " + "o's frequency is 7.507%\n" \
              "P is worth 3 - " + "p's frequency is 1.929%\n" + "Q is worth 10 - " + "q's frequency is 0.095%\n" + \
              "R is worth 1 - " + "r's frequency is 5.987%\n" + "S is worth 1 - " + "s's frequency is 6.327%\n" + \
              "T is worth 1 - " + "t's frequency is 9.056%\n" + "U is worth 1 - " + "u's frequency is 2.758%\n" + \
              "V is worth 4 - " + "v's frequency is 0.978%\n" + \
              "W is worth 4 - " + "w's frequency is 2.360%\n" + "X is worth 8 - " + "x's frequency is 0.150%\n" + \
              "Y is worth 4 - " + "y's frequency is 1.974%\n" + "Z is worth 10 - " + "z's frequency is 0.074%\n"
        print(msg)

    def Qstart(self):   # feature 2: List all the words start with "Q" but are not followed by a "u"
        #no input
        startQ=[]
        for word in self.__dictionary:
            letterList=word.strip()
            if letterList[0]=="q" and letterList[1]!="u":
                startQ.append(word)
        return startQ
        #output a list

    def twoLetters(self): # feature 3: Display all 2-letter words.
        twoLetterWord=[]
        for word in self.__dictionary:

            if len(word)==2:
                twoLetterWord.append(word)
        return twoLetterWord

    def inputLetter(self,letter):  # feature 4: Ask user for a letter and then show all the 3 letter words containing that given input tile.
        #no input
        threelettersList = []
        containLetters = []
        for line in self.__dictionary:
            if len(line) == 3:    # if the word is three letters word
                threelettersList.append(line)
                for item in threelettersList:
                    if letter in item:
                        containLetters.append(item)
        return containLetters
        # output a list

    def verifyExist(self,inputWord):   # feature 5: Word verifier: Ask user for a word and then verify that it exists within the Scrabble dictionary.
        #input a word as a string
        if inputWord in self.__dictionary:
                return True
        else:
                return False
        #output as boolean

    def containXZ(self,inputLetter):  # feature 6: ask a user for a letter and show all the words containing the letters "x" or "z" and the input tile.
        xz=[]
        for word in self.__dictionary:
            if inputLetter in word :
                if "x" in word or "z" in word:
                    xz.append(word)
        return xz

    def begin(self,input):   # feature 7: Ask user to enter one or more letters and then show all words that begin with that group of letters.
        # input as a string
        beginLetters=[]

        length=len(input)
        for word in self.__dictionary:
            word=word.strip()
            count=0
            num=0
            while num<length:
                if word[count]==input[count]:  #check from the first letter
                    count+=1
                num+=1
            if num==count:  #it proves that each letter in the input word corresponding to the same number of begin letters of the word in words.txt
                beginLetters.append(word)
        return beginLetters
        # output a list

    def end(self,input):    # feature 8: Ask user to enter one or more letters and then show all words that end with that group of letters.
        #input a string
        endLetters=[]
        inputLength = len(input)
        for word in self.__dictionary:
            word=word.strip()
            wordLetter=len(word)
            count=inputLength-1
            num=0
            i=1
            while num<inputLength:
                if word[wordLetter-i]==input[count]:  #check from the last letter
                    count-=1
                    i+=1
                num+=1
            if num==i-1:  #it proves that each letter in the input word corresponding to the same number of end letters of the word in words.txt
                endLetters.append(word)
        return endLetters
        #output as a string
    def pointValue(self,letter,pointvalues):   # feature 9: Whenever you display possible words to the user, also display the point values.
        # input a string and a dictionary
        length = len(letter)
        i = 0
        points = 0
        while i < length:
            points += pointvalues[letter[i]]
            i += 1
        return points
        #output an int












