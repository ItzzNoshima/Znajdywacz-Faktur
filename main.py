import os

clear = lambda: os.system("cls")

clear()

plik = input("Podaj nazwe pliku z fakturami: ")

clear()

kod = input("Podaj kod faktury do odszukania: ")

clear()

def znajdz_fakture(faktura):
    f = open(f"{plik}.txt", 'r', encoding='utf-8')

    lines = f.readlines()
    try:
        for line in lines:
            if faktura in line:
                dane = line.strip().split()

                transformed_surname = dane[1]
                transformed_surname = transformed_surname[:1] + transformed_surname[1:].lower()

                text_to_reply = f"Odszukano fakture!\nNumer Faktury: {dane[0]}\nImie: {dane[2]}\nNazwisko: {transformed_surname}\nData: {dane[3]}\nKwota do zapłaty: {dane[4]}PLN"
                return text_to_reply
    except:
        text_to_reply = "Nie znaleziono faktury o takim kodzie!"
        return text_to_reply

    f.close()

print(znajdz_fakture(kod))
os.system('pause')
