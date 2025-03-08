import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        t.handleAdd(txtIn.lower())
        print("Aggiunta!")
    elif int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        traduz = t.handleTranslate(txtIn.lower())
        print(traduz)
    elif int(txtIn) == 3:
        pass
    elif int(txtIn) == 4:
        break