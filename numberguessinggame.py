import random
print("Sayı Tahmin Etme Oyununa Hoşgeldiniz!!")
secilensayi= int(input("Lütfen oyunu oynamak istediğiniz aralığı en büyük sayıyı girerek belirtiniz: "))
tahmin_araligi=secilensayi
cevap=random.randint(1,tahmin_araligi)

tahmin= input("Bilgisayarımız Sayısını tutmuştur. Tuttuğu sayı 1 ve seçtiğiniz sayı arasındadır .Lütfen tahmininizi giriniz: ")
gecerlitahmin=int(tahmin)
while cevap != gecerlitahmin:
    if gecerlitahmin < cevap:
        print("Daha büyük bir sayı sanki :) ")
        yenitahmin = int(input("Aldığınız bilgiye göre tekrar tahmin ediniz: "))
        gecerlitahmin=yenitahmin
    elif gecerlitahmin > cevap:
        print("Biraz daha küçük bir sayı tahmin etmek isteyebilirsin :) ")
        yenitahmin = int(input("Aldığınız bilgiye göre tekrar tahmin ediniz: "))
        gecerlitahmin = yenitahmin
    else:
        break
print("Doğru tahmin ettiniz. Tebrikler")
