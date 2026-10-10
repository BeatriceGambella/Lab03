class Strumento:
    def __init__(self, codice_univoco, tipo, marca, anno_acquisto, valore_euro):
        #Uno strumento musicale conservato nel deposito
        self.__codice_univoco  = codice_univoco
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = int(anno_acquisto)
        self.__valore_euro = float(valore_euro)
        self.__disponibile = True

    @property
    def codice_univoco(self):              #rende leggibile l'attributo codice_univoco
        return self.__codice_univoco

    @property
    def marca(self):                       #rende leggibile l'attributo marca
        return self.__marca

    @property
    def disponibile(self):                 #rende leggibile l'attributo disponibile
        return self.__disponibile

    @disponibile.setter                    # rende modificabile l'attributo disponibile
    def disponibile(self, disponibile):
        self.__disponibile = disponibile

    #permette la stampa degli oggetti Strumento
    def __str__(self):
        return f"{self.__codice_univoco}, {self.__tipo}, {self.__marca}, {self.__anno_acquisto}, {self.__valore_euro:.2f}"

    #permette la stampa degli oggetti anche quando sono contenuti in una lista e viene stampata quest'ultima
    def __repr__(self):
        return self.__str__()