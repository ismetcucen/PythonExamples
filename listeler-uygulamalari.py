names = ["Ali", "Ya�mur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

#1 "Cenk" ismini listenin sonuna ekleyeniz.

names.append("Cenk")

#2 "Sena" de�erini listenin ba��na ekleyiniz.

names.insert(0,"Sena")

#3-4 "Deniz" isminin index nosu ve listeden siliniz. index=4

# names.remove("Deniz")
# index = names.index("Deniz")
# print(index)

#5 "Ali" listenin bir eleman� m�d�r?

# result = "Ali" in names
# result = names.index("Ali") - -1 den b�y�k bir de�er getiriyorsa liste i�indeki index nosunu verir.
#6 Liste elemanlar�n� ters �evirin.


names.reverse()


#7 Liste elemanlar�n� alfabetik olarak s�ralay�n�z.

names.sort()

#8 years listesini rakamsal b�y�kl��e g�re s�ralay�n�z.

years.sort()
years.reverse()



#9 karakter dizisini listeye �eviriniz.

#str = "Chevrolet, Dacia" 
# cars = "Chevrolet", "Dacia"
# cars = cars.split(",")
# print(cars)

#10 years dizisinin en b�y�k ve en k���k eleman� nedir?

# print(min(years))
# print(max(years))

#11 years dizisinde ka� tane 1998 de�eri vard�r?

# print(years.count(1998))

#12 years dizisinin t�m elemanlar�n� siliniz.

years.clear()

#13 Kullan�c�dan alaca��n�z 3 tane marka bilgisini bir listede saklay�n�z.

# cars.append(["Ford","Mercedes","BMW"])
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)


# print(names)
# print(years)
# print(cars)
# print(result)