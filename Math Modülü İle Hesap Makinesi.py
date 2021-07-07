import math
import time

print("""******************
      Hesap Makinesi Programına Hoşgeldiniz...
      
      İşlemler:
      
      Sin(x) = 1
      ----------
      Sqrt(x) = 2
      ----------
      Tan(x) = 3
      ----------
      Cos(x) = 4
      ----------
      Factorial(x) = 5
      ----------
      Log10(x) = 6
      ----------
      
      """)


while True:

    işlem = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz:")
    time.sleep(1)

    if (işlem == "1"):

        sayı = int(input("Lütfen Değeri Giriniz:"))

        math.sin(sayı)

        print("Sin(x) İşlem Sonucu:",math.sin(sayı))

    elif (işlem == "2"):

        sayı = int(input("Lütfen Değeri Giriniz:"))

        math.sqrt(sayı)

        print("Sqrt(x) İşlem Sonucu:", math.sqrt(sayı))

    elif (işlem == "3"):

        sayı = int(input("Lütfen Değeri Giriniz:"))

        math.tan(sayı)

        print("Tan(x) İşlem Sonucu:", math.tan(sayı))

    elif (işlem == "4"):

        sayı = int(input("Lütfen Değeri Giriniz:"))

        math.cos(sayı)

        print("Cos(x) İşlem Sonucu:", math.cos(sayı))

    elif (işlem == "5"):

        sayı = int(input("Lütfen Değeri Giriniz:"))

        math.factorial(sayı)

        print("Factorial(x) İşlem Sonucu:", math.factorial(sayı))

    elif (işlem == "6"):

        sayı = int(input("Lütfen Değeri Giriniz:"))

        math.log10(sayı)

        print("Log10(x) İşlem Sonucu:", math.log10(sayı))

    else:
        if (işlem == "7"):

            print("Lütfen İşlem Seçiniz...")
            break


