import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.italian = d.Dictionary().loadDictionary("resources/Italian.txt")
        self.english = d.Dictionary().loadDictionary("resources/English.txt")
        self.spanish = d.Dictionary().loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        pass

    def searchWord(self, words: list, language: str):
        lista_sbagliate = []
        if language == "Italian":
            dizionario = self.italian
        elif language == "English":
            dizionario = self.english
        else:
            dizionario = self.spanish

        for parola_datradurre in words:
            parola_rw = rw.RichWord(parola_datradurre)
            if parola_datradurre in dizionario:
                parola_rw.corretta = True
            else:
                lista_sbagliate.append(parola_rw)

        return lista_sbagliate

    def searchWordLinear(self, words: list, language: str):
        lista_sbagliate = []
        if language == "Italian":
            dizionario = self.italian
        elif language == "English":
            dizionario = self.english
        else:
            dizionario = self.spanish

        for parola_datradurre in words:
            parola_rw = rw.RichWord(parola_datradurre)
            corretto = False
            for parola_tradotta in dizionario:
                if parola_datradurre == parola_tradotta:
                    parola_rw.corretta = True
                    corretto = True
                    break
            if not corretto:
                lista_sbagliate.append(parola_rw)

        return lista_sbagliate

    def searchWordDichotomic(self, words: list, language: str):
        lista_sbagliate = []
        if language == "Italian":
            dizionario = self.italian
        elif language == "English":
            dizionario = self.english
        else:
            dizionario = self.spanish

        for parola_datradurre in words:
            parola_rw = rw.RichWord(parola_datradurre)
            corretto = False
            for parola_tradotta in dizionario:
                if parola_datradurre == parola_tradotta:
                    parola_rw.corretta = True
                    corretto = True
                    break
            if not corretto:
                lista_sbagliate.append(parola_rw)

        return lista_sbagliate




