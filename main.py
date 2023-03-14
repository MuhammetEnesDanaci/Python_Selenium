print("Merhaba Dünya")
baslik = "Taşıt Kredisi" #string
print(baslik)
#yorum satırı
vade = 36  #int değer
vade2 = "36"
print(vade*2)#72
print(vade+2)
print(vade2*2) #3636

#float,decimal,double
aylikOdeme = 200.50

#bool,boolean => true,false
yukselisteMi = True

#matematiksel operatörler
print(5 + 5)
print(13-9)
print(vade-7)
print(7*3)
print(75/5)

yeniVade=vade/2
fiyat=100
indirimliFiyat=fiyat-20

print(yeniVade)
print(fiyat)
print(indirimliFiyat)

# mod operatörü
print(10%2)
print(vade%5)

#mantıksal/karşılaştırma operatörleri
print(1==1)
print(1==2)

print("-----")

print(1>2)
print(3>2)
print(1>1)

print("-----")

print(1>=1)

print("-----")

print(1<2)
print(3<2)
print(1<1)
print(1<=1)

#CTRL + C seçilenleri yorum satırı yapar. CTRL + K yoruml satırını kaldırır
# print(1<2)
# print(3<2)
# print(1<1)
# print(1<=1)

print("-----")

print(1 != 1) #!= eşit değildir
print(1 != 2)

print("-----")

#or - and operatörleri
print("or - and operatörleri")
print((1 > 2) or (5>2))
print((1 > 2) and (5>2))
print((1 > 2) or (5>2) and (3>2))
print((5>2) or (1 > 2) and (3>2))
print((1 > 2) and (5>2) and (3>2))
print((2>1) or (1>2) and (3>2))

print("-----")

#karar yapıları (if - else)
print("karar yapıları")

sayi1=15
sayi2=15
#sayi1 sayi2 den büyük sayi1 büyük yazdır
if sayi1>sayi2:
    print("sayi1 sayi2 den büyüktür") #indent if bloğunun(süslü parantes içinin) bir tab boşluğu kadar içerde yazılması bu boşluk olduğu sürece aynı if bloğu içindesin
    print("hala if bloğu içerisindeyim")
elif sayi1 == sayi2:
    print("sayi1 sayi2 eşittir")
else:
    print("sayi2 sayi1 den büyüktür")
print("burası if bloğu dışı")
