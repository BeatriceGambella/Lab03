class Prestito:
    #codice del primo prestito che viene effettuato
    contatore = 1

    def __init__(self, data, codice_strumento, cognome_studente):
        #un prestito di uno strumento musicale effettuato dal deposito
        self.__codice_univoco = f"P{Prestito.contatore}"
        self.__data = data
        self.__codice_strumento = codice_strumento
        self.__cognome_studente = cognome_studente
        Prestito.contatore += 1

    @property
    def codice_univoco(self):                     #rende leggibile l'attributo codice_univoco
        return self.__codice_univoco

    @property
    def codice_strumento(self):                        # rende leggibile l'attributo codice_strumento
        return self.__codice_strumento

    # permette la stampa degli oggetti Prestito
    def __str__(self):
        return f"{self.__codice_univoco}, {self.__data}, {self.__codice_strumento}, {self.__cognome_studente}"

    # permette la stampa degli oggetti anche quando sono contenuti in una lista e viene stampata quest'ultima
    def __repr__(self):
        return self.__str__()