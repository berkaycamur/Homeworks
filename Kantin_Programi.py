import Kantin
urunler = {'cikolata':5, 'biskuvi': 10, 'kraker': 2}
islem_sec = int(input(("Ürün girmek için :1\n Kayıt olmak ve sıra almak için : 2\n Ürün satın almak için: 3\n Gün sonu hesabı almak için: 4 e basınız")))
if islem_sec == 1:
    Kantin.urun_girmek(urun_dict=urunler)
if islem_sec == 3:
    if Kantin.kayit_kontrol == 0:
        ikinci_kayit = int(input(('Lütfen öncelikle kaydınızı yapınız ve sıra numarası alınız.\n Sıra almak ve kayit olmak için 1 e basiniz.')))
        if ikinci_kayit == 1:
            Kantin.kayit_sira()
            Kantin.satin_al(urun_listesi=urunler)
    else:
        Kantin.satin_al(urun_listesi= urunler)
if islem_sec == 2:
    Kantin.kayit_sira()
    alisveris_devam_check = input('Satın alım yapmak ister misiniz? Evet = 1, Hayır = 2')
    if alisveris_devam_check == 1:
        Kantin.satin_al()
    else:
        pass
if islem_sec == 4:
    print(f" Bugünkü toplam kazanç: {Kantin.gun_sonu_hesapla()}")
