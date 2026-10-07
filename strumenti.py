class Strumento:
    def __init__(self, codice_univoco, tipo, marca, anno_acquisto, valore_euro):
        """Inizializza gli attributi e le strutture dati"""
        self.__codice_univoco  = codice_univoco
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = anno_acquisto
        self.__valore_euro = valore_euro