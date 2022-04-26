def tarjima_qil():

    a = None

    while a != "0":

        try:
            from deep_translator import GoogleTranslator
            matn = str(input("Matnni kiriting: "))
            til = str(input("Qaysi tilga tarjima qilmoqchisiz? "))
            translator = GoogleTranslator(source = "auto", target = til)
            tarjima = translator.translate(matn)

        except:
            print("Tilni xato kiritdiz. Iltimos qaytadan urinib ko'ring! ")

        else:

            print(tarjima)

        a = input("Davom etamizmi? Tanlang:\nHa - 1\nYo'q - 0\nKiriting: ")
    
    print("Dasturdan foydalanganiz uchun tashakkur!")

tarjima_qil()