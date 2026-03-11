class Dictionary:
    def __init__(self):
        self._lista = []

    def loadDictionary(self, path: str):
        with open(path, 'r', encoding = "utf-8") as file:
            for line in file:
                self._lista.append(line.strip())
        return self._lista

    def printAll(self):
        for parola in self._lista:
            print(parola)

    @property
    def dict(self):
        return self._lista
