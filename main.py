meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }

word = input("Ketik kata yang tidak Kamu mengerti:") .upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Maaf, saat ini kami tidak memiliki kamus untuk kata ini namun kami akan terus memperluas kamus kami")
