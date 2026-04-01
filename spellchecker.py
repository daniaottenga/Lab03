import time
import multiDictionary as md

class SpellChecker:

    def __init__(self, multidict = md.MultiDictionary()):
        self.multidict = multidict

    def handleSentence(self, txtIn: str, language: str):
        txtIn = replaceChars(txtIn)
        lista = txtIn.split()

        inizio = time.time()
        lista_sbagliate = self.multidict.searchWord(lista, language)
        fine = time.time()
        stampa(lista_sbagliate, "contains", fine, inizio)
        lista_sbagliate.clear()

        inizio = time.time()
        lista_sbagliate = self.multidict.searchWordLinear(lista, language)
        fine = time.time()
        stampa(lista_sbagliate, "Linear search", fine, inizio)
        lista_sbagliate.clear()

        inizio = time.time()
        lista_sbagliate = self.multidict.searchWordDichotomic(lista, language)
        fine = time.time()
        stampa(lista_sbagliate, "Dichotomic search", fine, inizio)
        lista_sbagliate.clear()


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`?*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text.lower()

def stampa(lista: list, using: str, fine, inizio):
    print(f"Using {using}")
    for parola in lista:
        print(parola)
    print(f"Parole sbagliate: {len(lista)}\n" +
          f"Tempo di processamento: {(fine - inizio):.6f}\n" +
          "______________________________\n")
