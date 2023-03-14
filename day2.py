faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)#vade değişkeni string ten int e çevrildi.

faiz = str(faiz)
print(type(faiz))


# vade =input("Lütfen vade sayısı giriniz : ")
#vade =int(input("Lütfen vade sayısı giriniz : "))
vade=30
print(type(vade))
# print(vade+12)
# print(int(vade)+12)
vade = vade +12

#string interpolation
#seçtiğiniz vade sonucu ortaya çıkan vade

print("seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi=vade))

isim = "Halit"
metin = "Merhaba {name}".format(name=isim)
print(metin)

#f-string
# isim2 = input("isim girin : ")
# metin2 = f"Hoşgeldiniz {isim2}"
# print(metin2)

#listeler
dizi = ["ihtiyaç kredisi", 10 , 5.2 , True]
print(dizi)
print("----------------")
krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
print(krediler)
print("dizinin uzunluğu : " + str(len(krediler)))
print(krediler[0])
print(krediler[1])
print(krediler[2])

#eleman ekleme
krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredi")
print(krediler)

#yazılan indexteki elemanı siler. index vermezsek son elemanı siler
krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredi")
print(krediler)

#index ile değil değer ile çalışır.aynısından 2 tane varsa indexe göre ilk olanı siler
krediler.remove("Taşıt Kredisi")
print(krediler)

#aynı anda birden fazla eleman ekleme
krediler.extend(["Y Kredi","Z Kredisi"])
print(krediler)

#DÖNGÜLER
#for
for i in range(10):
    print("sayı :")
    print(i)

print("----------------")

for i in range(5,11):#5 ten başla 11 e kadar
    print(i)

print("----------------")

for i in range(0,51,10):#0 dan 51 e 10 arttırarak
    print(i)
    
print("----------------")

for i in range(5,10):#5 ten başla 10 a kadar
    print(i)

print("----------------")

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)

print("----------------")

for i in range(len(krediler)):
    print(krediler[i])

print("----------------")

#while döngüsü
i=0
while i<10:
    print("x")
    i+=1
print("y")

print("----------------")

while True:
    print("X")
    break

print("----------------")

i=0
while i<len(krediler):
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i+=1

print("----------------")

#fonksiyonlar
fiyat = 100
indirim = 20
#definition
def calculate(): #geriye değer döndürmeyen fonksiyon
    print(100-20)

def calculateWithParams(fiyat,indirim): #parametreli fonksiyon
    print(fiyat-indirim)

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)

print("----------------")

def sayHello(name):
    print(f"Merhaba {name}")

sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")

print("----------------")

#geriye değer döndüren fonksiyon
def calculateAndReturn(price,discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat+10)

#void(değer döndürmeyen fonksiyon)
def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndreturn(price,discount):
    return price-discount

print("----------------")

fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndreturn(300,100)

print(fonk1)
print(fonk2)
