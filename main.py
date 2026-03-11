import spellchecker

sc = spellchecker.SpellChecker()

txtIn = ""

while txtIn != 4:

    sc.printMenu()
    while not txtIn.isdigit():
        txtIn = input()

    # 1. parole con errori di ortografia usando contains, ricerca lineare e la ricerca dicotomica
    # 2. numero di parole errate
    # 3. tempo di calcolo

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        print("______________________________")
        sc.handleSentence(txtIn, "Italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        print("______________________________")
        sc.handleSentence(txtIn, "English")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        print("______________________________")
        sc.handleSentence(txtIn, "Spanish")
        continue

    if int(txtIn) == 4:
        break


