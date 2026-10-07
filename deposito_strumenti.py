from strumenti import Strumento
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile


    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, responsabile: str):
        self.__responsabile = responsabile
        print("Il responsabile è stato aggiornato correttamente!")


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            infile = open(file_path, "r")     #apertura file
            for line in infile:               #leggo tutte le righe del file
                line = line.rstrip()          #per ogni riga elimina i caratteri bianchi finali

                if line == "":                #evito che mi dia errore se una riga è vuota
                    continue

                strumenti = []
                dati = line.split(",")
                strumenti.append(Strumento(dati[0], dati[1], dati[2], dati[3], dati[4]))

            infile.close()                    #chiusura del file

        except FileNotFoundError:             #se non viene trovato un file, il programma restituisce None
            return None

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
