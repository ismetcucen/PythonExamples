cars = ["BMW", "Mercedes", "Opel", "Mazda"]
print(cars)

# 2 Liste ka� elemanl�d�r?

cars = ["BMW", "Mercedes", "Opel", "Mazda"]
print(len(cars))

# 3 Listenin ilk ve son eleman� nedir?

cars = ["BMW", "Mercedes", "Opel", "Mazda"]
print(cars[0])
print(cars[3])

# 4 Mazda de�erini, Toyota ile de�i�tirin.
cars = ["BMW", "Mercedes", "Opel", "Mazda"]
cars[-1] = "Toyota"
print(cars)


#5 Mercedes listenin bir eleman� m�d�r?
cars = ["BMW", "Mercedes", "Opel", "Mazda"]
result = "Mercedes" in cars
print(result)

#6
cars = ["BMW", "Mercedes", "Opel", "Mazda"]
result = cars[-2]
print(result)

#7
cars = ["BMW", "Mercedes", "Opel", "Mazda"]
result = cars[0:3]
print(result)

#8 Listenin son 2 eleman� yerine "Toyota" ve "Renault"de�erlerini ekleyin.
cars = ["BMW", "Mercedes", "Opel", "Mazda"]
cars[-2] = "Toyota"
cars[-1] = "Renault"
# ya da 
cars[-2:] = ["Toyota","Renault"]
print(cars)


#9 Listenin �zerine "Audi" ve "Nissan" modellerini ekleyin.
cars = ["BMW", "Mercedes", "Opel", "Mazda"]
newcars = ["Audi","Nissan"]
result = cars + newcars
print(result)
# ya da
result = cars + ["audi","nissan"]
print(result)

#10 Listenin son eleman�n� silin.

cars = ["BMW", "Mercedes", "Opel", "Mazda","Audi","Nissan"]
del cars[-1] 
print(cars)

#11 Liste elemanlar�n� tersten yazd�r�n�z.
cars = ["BMW", "Mercedes", "Opel", "Mazda","Audi","Nissan"]
cars.reverse()
print(cars)

#12 A�a��daki verileri bir liste i�inde saklay�n�z.

studentA = ["Yi�it","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

print(studentA)
print(studentB)
print(studentC)

result = f"{studentA[0]} {studentA[1]} {2020-studentA[2]} ya��nda ve not ortalamas� {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3} "
print(result) 