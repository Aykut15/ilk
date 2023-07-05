meme_dict = {
           "LOL": "Sesli Güldüm",
           "CRİNGE": "Utanç Verici",
           "CREEPY": "Korkunç",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
        print("Kelime Bulunmadı!")
