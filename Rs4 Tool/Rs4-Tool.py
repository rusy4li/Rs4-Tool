try:
    import requests
except ImportError:
    print(">>> 'requests' modül hatası!")
try:
    import os
except ImportError:
    print(">>> 'os' modül hatası!")
try:
    import time
except ImportError:
    print(">>> 'time' modül hatası!")
try:
    import colorama
    from colorama import Fore, Style
    colorama.init()
except ImportError:
    print(">>> 'colorama' modül hatası!")
try:
    import hashlib as hasher
except ImportError:
    print(">>> 'hashlib' modül hatası!")


# -*- coding:utf-8 -*-
#!/usr/bin/env python

########################################################

# Bu tool elitehackz.org için rusy4li tarafından kodlanmıştır!
# Github Hesabım: https://github.com/rusy4li
# Websitem: https://rusy4.xyz/
# İnstagram Hesabım: https://instagram.com/rusy4li

########################################################

user = "rusy4li"
license = "rusy4li tarafından kodlanmıştır!"

#######################################################


def run():
    print()
    print()
    input(" Devam etmek için herhangi bir tuşa bas...")
    os.system("cls")


if user != "rusy4li" or license != "rusy4li tarafından kodlanmıştır!":
    while True:
        print(""" Elitehackz.org""")
        time.sleep(1.5)
        os.system("cls")

# Run
os.system("cls")
# print(Style.RESET_ALL)
while True:
    # http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Rs4%20Tool
    print(Fore.RED+"""
                                ██████╗ ███████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗
                                ██╔══██╗██╔════╝██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║
                                ██████╔╝███████╗███████║       ██║   ██║   ██║██║   ██║██║
                                ██╔══██╗╚════██║╚════██║       ██║   ██║   ██║██║   ██║██║
                                ██║  ██║███████║     ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
                                ╚═╝  ╚═╝╚══════╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

    """)
    print(
        "                                       [#]Rs4 PanelFinder    - Admin Panel Bulucu")
    print(
        "                                       [#]Developer          - rusy4li")
    print(
        "                                       [#]Website            - rusy4.xyz")
    print(
        "                                       [#]GitHub             - github.com/rusy4li")

    print("\n")
    ###############
    print(" [1] MD5 Hash alma")
    print(" [2] MD5 Hash Kırma")
    print(" [3] İp sorgu")
    print(" [4] Admin Panel Bulma")
    print(" [5] Txt Patlatma")
    sorgu = input(" > ")
    print()

    # MD5 Hash Alma
    if (sorgu == "1"):
        # Md 5 cracker
        sifreleyici = hasher.md5()
        print(" [!] Şifrelemek istediğiniz metin")
        sorgu_metin = input(" > ")
        metin = sorgu_metin
        sifreleyici.update(metin.encode("utf-8"))
        hash = sifreleyici.hexdigest()
        print(" [!] Şifrelenen Metin >> ", hash)

    # MD5 Hash Kırma
    elif (sorgu == "2"):
        print(" [+] Kırılacak MD5 Hash")
        sorgu_md5 = input(" > ")
        response = requests.get(
            'http://www.nitrxgen.net/md5db/' + sorgu_md5).text
        print(" [!] Md5 Hash Sonuç >> ", response)

    # İp Sorgu Yapma
    elif (sorgu == "3"):
        print(" [+] Sorgulamak istediğiniz ip adresi")
        sorgu_ip = input(" > ")
        print()
        Ulke = requests.get(
            "https://ipinfo.io/{}/country/".format(sorgu_ip)).text
        Sehir = requests.get(
            "https://ipinfo.io/{}/region/".format(sorgu_ip)).text
        Bolge = requests.get(
            "https://ipinfo.io/{}/postal/".format(sorgu_ip)).text
        Lokasyon = requests.get(
            "https://ipinfo.io/{}/loc/".format(sorgu_ip)).text
        Zaman = requests.get(
            "https://ipinfo.io/{}/timezone/".format(sorgu_ip)).text
        Organizasyon = requests.get(
            "https://ipinfo.io/{}/org/".format(sorgu_ip)).text
        print(" [!] Sonuç:")
        print(" Ülke:", Ulke)
        print(" Şehir:", Sehir)
        print(" Bölge:", Bolge)
        print(" Lokasyon:", Lokasyon)
        print(" Zaman Dilimi:", Zaman)
        print(" Organizasyon:", Organizasyon)
        print()
        print(" [!] Sorgu sonucunu txt'ye kaydetmek istermisiniz [evet],[hayır]")
        sorgu_txt_kayit = str(input(" > "))
        if sorgu_txt_kayit.lower() == "evet":
            print(" [!] Dosya ismi")
            sorgu_dosya_adi = input(" > ")
            with open(sorgu_dosya_adi+".txt", "w", encoding='utf-8') as f:
                bilgi = [Ulke, Sehir, Bolge, Lokasyon, Zaman, Organizasyon]
                for giris in bilgi:
                    f.write(giris)
                    f.write("\n")
                print(" [!] Kayıt Başarılı")
                print()

    # Admin Panel Bulma
    elif (sorgu == "4"):
        i = 0
        print(
            " [!] 'https://' veya 'http://' kullanmanız gerekiyor! Ve sonuna '/' koymayı unutmayınız!")
        print(" [+] Lütfen Site Alan Adını Giriniz!")
        while i == 0:
            sorgu_site = input(" > ")
            tam_site = sorgu_site.strip()
            ###
            if (tam_site == ""):
                print(" [-] Lütfen Site Alan Adını Giriniz!")
            else:
                i += 1
                print(" [1] Hızlı Tarama")
                print(" [2] Full Tarama")
                sorgu_tarama_türü = int(input(" > "))

                # Tarama Başlıyor...
                if (sorgu_tarama_türü == 2):
                    print(" [!] Tarama Başlıyor...")
                    print()
                    with open("wordlist/full.txt", "r", encoding='utf-8') as f:
                        for satir in f.readlines():
                            site = tam_site+satir
                            site_strip = site.strip()
                            istek = requests.get(site_strip)
                            if (istek.status_code == 200):
                                print(" [!] Admin Panel Bulundu >>",
                                      site_strip)
                                print(" -------------")
                    print(" [!] Tarama Bitmiştir!")
                ####
                else:
                    print(" [!] Tarama Başlıyor...")
                    print()
                    with open("wordlist/fast.txt", "r", encoding='utf-8') as f:
                        for satir in f.readlines():
                            site = tam_site+satir
                            site_strip = site.strip()
                            istek = requests.get(site_strip)
                            if (istek.status_code == 200):
                                print(" [!] Admin Panel Bulundu >>",
                                      site_strip)
                                print(" -------------")
                    print(" [!] Tarama Bitmiştir!")

    # Txt Patlatma
    elif (sorgu == "5"):
        print(
            " [!] 'https://' veya 'http://' kullanmanız gerekiyor! Ve sonuna '/' koymayı unutmayınız!")
        print(" [+] Lütfen Txt'sini Patlatmak İstediğiniz Site'nin Alan Adını Giriniz!")
        i = 0
        while i == 0:
            sorgu_site = input(" > ")
            tam_site = sorgu_site.strip()
            ###
            if (tam_site == ""):
                print(" [-] Lütfen Site Alan Adını Giriniz!")
            else:
                i += 1
                print(" [+] Wordlist yolu belirtin lütfen!")
                sorgu_txt = input(" > ")

                try:
                    print(" [!] Tarama Başlıyor...")
                    print()
                    with open(sorgu_txt, "r", encoding='utf-8') as f:
                        for satir in f.readlines():
                            site = tam_site+satir
                            site_strip = site.strip()
                            istek = requests.get(site_strip)
                            if (istek.status_code == 200):
                                print(" [!] Txt Bulundu >>", site_strip)
                                print("-------------")
                except FileNotFoundError:
                    print(" [-] Belirttiğiniz Yolda Wordlist bulunmuyor!")
                finally:
                    print(" [!] Tarama Bitmiştir!")

    # Başa sarıyor!
    run()
