import random

def benibul_oyunu():
    sayi = random.randint(1, 100)
    tahminler = []

    print("1 ve 100 arasında sayı tuttum.")
    while True:
        tahmin = int(input("Tahmininizi söyleyebilir misiniz? "))
        tahminler.append(tahmin)

        if tahmin == sayi:
            print("Tebrikler, doğru tahmin ettiniz! Tahminleriniz: ", tahminler)
            break
        elif tahmin < sayi:
            print("Daha yüksek bir sayı deneyin.")
        else:
            print("Daha düşük bir sayı deneyin.")

benibul_oyunu()
