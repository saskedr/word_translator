meme_tradutor = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "СКАМ": "обман"
            }
word = input("Введите непонятное слово").upper()
if word in meme_tradutor.keys():
    print(meme_tradutor.get(word))
else:
    print("такого слово нет")
