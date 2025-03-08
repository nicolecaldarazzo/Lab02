class Dictionary:
    def __init__(self,dizionario={}):
       self.dizionario = dizionario

    def addWord(self,aliena, traduzione):
        self.dizionario.update({aliena: traduzione})

    def translate(self,aliena):
        traduzione = self.diz[aliena]
        return traduzione

    def translateWordWildCard(self):
        pass

    def loadDizionario(self, diz):
        self.diz = diz