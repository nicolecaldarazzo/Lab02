from dictionary import Dictionary
class Translator:

    def __init__(self):
        self.d = Dictionary()

    def printMenu(self):
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit\n")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        input_file=open(dict,"r",encoding='utf-8')
        riga=input_file.readline()
        dizionario = {}
        while riga!="":
            riga.split(" ")
            dizionario.update({riga.split(" ")[0]: riga.split(" ")[1]})
            riga = input_file.readline()
        input_file.close()
        self.d.loadDizionario(dizionario)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        campi = entry.split(" ")
        self.d.addWord(campi[0],campi[1])

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        trad = self.d.translate(query)
        return trad

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass