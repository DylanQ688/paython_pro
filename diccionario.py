meme_dict = {"CRINGE": "Algo excepcionalmente raro o embarazoso"}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("no tenemos la palabra que busca")
