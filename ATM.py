import time
users = {
    'ahmet': {'sifre': '1500', 'bakiye': 15520},
    'cenk': {'sifre': '2700', 'bakiye': 27560},
    'burak': {'sifre': '4676', 'bakiye': 465216},
    'beril': {'sifre': '5683', 'bakiye': 56273},
    'ayşe': {'sifre': '6532', 'bakiye': 6532005},
}

def giris_yap():
    hak = 3
    while hak > 0:
        kullanici = input("İsminizi Giriniz: ")
        sifre = input("Şifrenizi Giriniz: ")
        if kullanici in users and users[kullanici]['sifre'] == sifre:
            print("Giriş başarılı...")
            return kullanici
        else:
            hak -= 1
            print(f"Lütfen kullanıcı adı veya şifrenizi kontrol ediniz! {hak} hakkınız kaldı.")
    print(f"Sayın {kullanici} Deneme hakkınız kalmamıştır.")
    return None

def ana_program():
    kullanici = giris_yap()
    if kullanici:
        while True:
            print("\n1. Bakiye kontrol et.")
            print("2. Para çek.")
            print("3. Para yatır.")
            print("4. Çıkış yap")
            secim = input("Bir seçim yapınız (1/2/3/4): ")

            if secim == '1':
                bakiye_kontrol(kullanici)
            elif secim == '2':
                para_cek(kullanici)
            elif secim == '3':
                para_yatir(kullanici)
            elif secim == '4':
                cikis_yap()
                break
            else:
                print("Lütfen geçerli bir seçenek seçiniz!!!")

def bakiye_kontrol(kullanici):
    print(f"Hesap bakiyeniz {users[kullanici]['bakiye']} TL.")

def para_cek(kullanici):
    cek = float(input("Çekmek istediğiniz miktarı giriniz: "))
    if cek > users[kullanici]['bakiye']:
        print("Yeterli bakiyeniz yok.")
    else:
        users[kullanici]['bakiye'] -= cek
        print(f"Hesabınızdan {cek} TL miktarında para çekildi. Hesap bakiyeniz {users[kullanici]['bakiye']} TL'dir.")

def para_yatir(kullanici):
    yatir = float(input("Yatırmak istediğiniz para miktarını giriniz: "))
    users[kullanici]['bakiye'] += yatir
    print(f"Yatırılan miktar {yatir} TL'dir. Hesap bakiyeniz {users[kullanici]['bakiye']} TL'dir.")

def cikis_yap():
    print("Çıkış yapılıyor...")
    time.sleep(1.0)
    print("Çıkış yapıldı...")


if __name__ == "__main__":
    ana_program()
