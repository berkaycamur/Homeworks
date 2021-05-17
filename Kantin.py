import random
toplam = 0
kayit_kisi_sayisi = 0
urunlerr = {'a':3, 'b':4}
kayit_kontrol = 0
def urun_girmek(urun_dict):
    while True:
        key = input('Lütfen ürün ismini giriniz: ')
        value = input('Lütfen ürün fiyatını giriniz: ')
        urun_dict.update({key: value})
        devam_mi = int(input("Ürün eklemeye devam etmek ister misiniz ? "))
        if devam_mi == 1:
            continue
        else:
            break


def kayit_sira():
    sira_no = random.randint(0,48)



def gun_sonu_hesapla():
    return toplam


def satin_al(**urun_listesi):
    while True:
        urun_sec = input("Hangi ürünü satın almak istersiniz ? Reyondaki ürünler: ")
        for i in urun_listesi.keys():
            print(i)
        toplam = urun_listesi[i] + toplam
        devam_check = int(input('Alışverişe devam etmek ister misiniz? 1= Evet, 2= Hayır'))
        if devam_check == 1:
            continue
        elif devam_check == 2:
            break