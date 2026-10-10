from operator import attrgetter
from prestito import Prestito
from strumento import Strumento        #importo la classe Strumento

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile
        self.strumenti = []
        self.prestiti = []


    @property                                 #rende leggibile l'attributo responsabile
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter                      #rende modificabile l'attributo responsabile
    def responsabile(self, responsabile):
        self.__responsabile = responsabile


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        self.strumenti.clear()                #ogni volta che viene caricato un nuovo file svuota la lista contente gli
                                              #strumenti del file precedente
        try:
            infile = open(file_path, "r")     #apertura file
            for line in infile:               #leggo tutte le righe del file
                line = line.strip()           #per ogni riga elimina i caratteri in eccesso all'inizio e alla fine

                if line == "":                #evito che mi dia errore se una riga è vuota
                    continue

                dati = line.split(",")        #trasforma ogni riga del file in una lista
                # creo una lista contente ogni strumento(oggetto) contenuto nel file inserito
                self.strumenti.append(Strumento(dati[0], dati[1], dati[2], int(dati[3]), float(dati[4])))

            infile.close()                    #chiusura del file
            return self.strumenti             #ritorna la lista contenente gli strumenti

        except FileNotFoundError:
            raise Exception(f"File {file_path} non trovato.")  #se il file non viene trovato viene scatenata l'eccezione

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        ultimo_strumento = self.strumenti[-1]                #considero l'ultimo oggetto all'interno della lista
        numero = int(ultimo_strumento.codice_univoco[1:])    #considero il numero del codice_univoco dell'ultimo oggetto
        codice = "S"+str(numero+1)                           #creo il codice univoco del nuovo strumento

        nuovo_strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)  #creo un nuovo oggetto per il nuovo strumento
        self.strumenti.append(nuovo_strumento)       #aggiungo il nuovo strumento alla lista

        return nuovo_strumento       #ritorna il nuovo strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti, key=attrgetter('marca'))   #ritorna la lista degli strumenti ordinati
                                                                 #alfabeticamente per la marca (la chiave di ordinamento)
    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        strumento_prestito = None          #lo strumento da prestare non è ancora stato trovato

        for s in self.strumenti:           #viene controllato se uno degli strumenti presenti nel deposito sia quello
            if s.codice_univoco == id_strumento:       #richiesto per il prestito
                strumento_prestito = s

                if not strumento_prestito.disponibile:      #se viene trovato lo strumento richiesto ma questo è già in
                    raise Exception(f"Lo strumento {id_strumento} e gia in prestito")   #prestito viene scatenata un'eccezione
                break

        if strumento_prestito is None:    #se lo strumento richiesto non è presente nel deposito viene scatenata
            raise Exception(f"Lo strumento {id_strumento} non si trova nel deposito")    #un'eccezione

        prestito = Prestito(data, id_strumento, cognome_allievo)     #creazione dell'oggetto prestito
        strumento_prestito.disponibile = False                       #aggiornamento dello stato dello strumento prestato
        self.prestiti.append(prestito)                               #viene aggiunto il prestito appena fatto alla lista
        return prestito                                                   # dei prestiti

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        prestito_finito = None             #il prestito da terminare non è ancora stato trovato

        for p in self.prestiti:            #viene controllato se uno dei prestiti presenti già effettuati sia quello
            if p.codice_univoco == id_prestito:    #che si vuole terminare
                prestito_finito = p

                for s in self.strumenti:
                    if s.codice_univoco == prestito_finito.codice_strumento:
                        s.disponibile = True     #se viene terminato il prestito viene aggiornato lo stato dello strumento
                        break                    #che era in prestito
                break

        if prestito_finito is None:              #se il prestito che si vuole terminare non è presente tra quelli effettuati
            raise Exception(f"Prestito {id_prestito} non trovato.")    #viene scatenata un'eccezione

        self.prestiti.remove(prestito_finito)    #il prestito viene cancellato dalla lista dei prestiti fatti
