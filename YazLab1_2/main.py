import csv
import string
import pandas
import threading
import timeit
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from urunEkle import *

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()


dataFrame = pandas.read_csv('cleandata.csv')
dataFrame = dataFrame.head(50)


def karsilastirma(ilk_indeks, ikinci_indeks):

    enbuyuk = len(ilk_indeks)
    if (len(ikinci_indeks) > len(ilk_indeks)):
        enbuyuk = len(ikinci_indeks)

    benzer_sayisi = 0

    for item1 in ilk_indeks:

        for item2 in ikinci_indeks:

            if (item1 == item2):
                benzer_sayisi = benzer_sayisi + 1

    sonuc = (benzer_sayisi/enbuyuk) * 100
    if (sonuc == 125.0):
        sonuc = 100.0
    return sonuc


def product_kiyaslama(baslangic, bitis):

    #start = timeit.default_timer()

    product = dataFrame['Product']
    # print(product)

    for sayi in range(baslangic, bitis):

        ilk_indeks = product.iloc[sayi].lower().strip()
        parcalanan_birinci = ilk_indeks.split()

        for sayi2 in range(len(product)):

            ikinci_indeks = product.iloc[sayi2].lower().strip()
            parcalanan_ikinci = ikinci_indeks.split(" ")

            benzerlik_orani = karsilastirma(
                parcalanan_birinci, parcalanan_ikinci)
            print(
                f"İlk indeks : {ilk_indeks} , İkinci indeks :{ikinci_indeks} , Benzerlik oranları : {benzerlik_orani} | ")


def product_kiyaslama_oranli(oran, baslangic, bitis):

    #start = timeit.default_timer()

    product = dataFrame['Product']
    # print(product)

    for sayi in range(baslangic, bitis):

        ilk_indeks = product.iloc[sayi].lower().strip()
        parcalanan_birinci = ilk_indeks.split()

        for sayi2 in range(len(product)):

            ikinci_indeks = product.iloc[sayi2].lower().strip()
            parcalanan_ikinci = ikinci_indeks.split(" ")

            benzerlik_orani = karsilastirma(
                parcalanan_birinci, parcalanan_ikinci)
            if (benzerlik_orani > oran):
                print(
                    f"İlk indeks : {ilk_indeks} , İkinci indeks :{ikinci_indeks} , Benzerlik oranları : {benzerlik_orani} | ")

    #stop = timeit.default_timer()
    #print('Product Kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def issue_kiyaslama(baslangic, bitis):

    #start = timeit.default_timer()
    issue = dataFrame['Issue']

    for sayi in range(baslangic, bitis):

        ilk_indeks = issue.iloc[sayi].lower().strip()
        parcalanan_birinci = ilk_indeks.split()

        for sayi2 in range(len(issue)):

            ikinci_indeks = issue.iloc[sayi2].lower().strip()
            parcalanan_ikinci = ikinci_indeks.split(" ")

            benzerlik_orani = karsilastirma(
                parcalanan_birinci, parcalanan_ikinci)
            print(
                f"İlk indeks : {ilk_indeks} , İkinci indeks :{ikinci_indeks} , Benzerlik oranları : {benzerlik_orani} | ")

    #stop = timeit.default_timer()
    #print('Issue kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def company_kiyaslama(baslangic, bitis):

    #start = timeit.default_timer()

    company = dataFrame['Company']

    for sayi in range(baslangic, bitis):

        ilk_indeks = company.iloc[sayi].lower().strip()
        parcalanan_birinci = ilk_indeks.split()

        for sayi2 in range(len(company)):

            ikinci_indeks = company.iloc[sayi2].lower().strip()
            parcalanan_ikinci = ikinci_indeks.split(" ")

            benzerlik_orani = karsilastirma(
                parcalanan_birinci, parcalanan_ikinci)
            print(
                f"İlk indeks : {ilk_indeks} , İkinci indeks :{ikinci_indeks} , Benzerlik oranları : {benzerlik_orani} | ")

    #stop = timeit.default_timer()
    #print('Company kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def state_kiyaslama(baslangic, bitis):

    #start = timeit.default_timer()

    state = dataFrame['State']

    for sayi in range(baslangic, bitis):

        ilk_indeks = state.iloc[sayi].lower().strip()
        parcalanan_birinci = ilk_indeks.split()

        for sayi2 in range(len(state)):

            ikinci_indeks = state.iloc[sayi2].lower().strip()
            parcalanan_ikinci = ikinci_indeks.split(" ")

            benzerlik_orani = karsilastirma(
                parcalanan_birinci, parcalanan_ikinci)
            print(
                f"İlk indeks : {ilk_indeks} , İkinci indeks :{ikinci_indeks} , Benzerlik oranları : {benzerlik_orani} | ")

    #stop = timeit.default_timer()
    #print('State kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def zipcode_kiyaslama(baslangic, bitis):

    #start = timeit.default_timer()

    zipcode = dataFrame['ZIP code']

    for sayi in range(baslangic, bitis):

        ilk_indeks = zipcode.iloc[sayi].lower().strip()
        parcalanan_birinci = ilk_indeks.split()

        for sayi2 in range(len(zipcode)):

            ikinci_indeks = zipcode.iloc[sayi2].lower().strip()
            parcalanan_ikinci = ikinci_indeks.split(" ")

            benzerlik_orani = karsilastirma(
                parcalanan_birinci, parcalanan_ikinci)
            print(
                f"İlk indeks : {ilk_indeks} , İkinci indeks :{ikinci_indeks} , Benzerlik oranları : {benzerlik_orani} | ")

    #stop = timeit.default_timer()
    #print('Zipcode kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def thread_product(thread_sayisi):

    start = timeit.default_timer()

    i = 0
    liste = []
    kat = int(len(dataFrame)/thread_sayisi)
    baslangic = 0
    bitis = kat
    while (i < thread_sayisi):

        liste.append(threading.Thread(
            target=product_kiyaslama, args=(baslangic, bitis)))
        i = i + 1
        baslangic = baslangic + kat
        bitis = bitis + kat
    for j in liste:
        j.start()

    stop = timeit.default_timer()
    print('Multithreading uygulanmış product kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def thread_product_oranli(thread_sayisi, oran):

    start = timeit.default_timer()

    i = 0
    liste = []
    kat = int(len(dataFrame)/thread_sayisi)
    baslangic = 0
    bitis = kat
    while (i < thread_sayisi):

        liste.append(threading.Thread(
            target=product_kiyaslama_oranli, args=(oran, baslangic, bitis)))
        i = i + 1
        baslangic = baslangic + kat
        bitis = bitis + kat
    for j in liste:
        j.start()

    stop = timeit.default_timer()
    print('Multithreading uygulanmış product kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def thread_issue(thread_sayisi):

    start = timeit.default_timer()
    i = 0
    liste = []
    kat = int(len(dataFrame)/thread_sayisi)
    baslangic = 0
    bitis = kat
    while (i < thread_sayisi):

        liste.append(threading.Thread(
            target=issue_kiyaslama, args=(baslangic, bitis)))
        i = i + 1
        baslangic = baslangic + kat
        bitis = bitis + kat
    for j in liste:
        j.start()

    stop = timeit.default_timer()
    print('Multithreading uygulanmış issue kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def thread_company(thread_sayisi):

    start = timeit.default_timer()

    i = 0
    liste = []
    kat = int(len(dataFrame)/thread_sayisi)
    baslangic = 0
    bitis = kat
    while (i < thread_sayisi):

        liste.append(threading.Thread(
            target=company_kiyaslama, args=(baslangic, bitis)))
        i = i + 1
        baslangic = baslangic + kat
        bitis = bitis + kat
    for j in liste:
        j.start()

    stop = timeit.default_timer()
    print('Multithreading uygulanmış company kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def thread_state(thread_sayisi):

    start = timeit.default_timer()

    i = 0
    liste = []
    kat = int(len(dataFrame)/thread_sayisi)
    baslangic = 0
    bitis = kat
    while (i < thread_sayisi):

        liste.append(threading.Thread(
            target=state_kiyaslama, args=(baslangic, bitis)))
        i = i + 1
        baslangic = baslangic + kat
        bitis = bitis + kat
    for j in liste:
        j.start()

    stop = timeit.default_timer()
    print('Multithreading uygulanmış state kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)


def thread_zipcode(thread_sayisi):

    start = timeit.default_timer()

    i = 0
    liste = []
    kat = int(len(dataFrame)/thread_sayisi)
    baslangic = 0
    bitis = kat
    while (i < thread_sayisi):

        liste.append(threading.Thread(
            target=zipcode_kiyaslama, args=(baslangic, bitis)))
        i = i + 1
        baslangic = baslangic + kat
        bitis = bitis + kat
    for j in liste:
        j.start()

    stop = timeit.default_timer()
    print('Multithreading uygulanmış zipcode kıyaslama fonksiyonunun toplam çalışma süresi : ', stop - start)

# thread_product_oranli(5,60)
# thread_product_oranli(5,60)


def product_cekirdekleme():
    cekirdek_sayisi = int(ui.lineProduct.text())
    thread_product(cekirdek_sayisi)


def issue_cekirdekleme():
    cekirdek_sayisi = int(ui.lineIssue.text())
    thread_issue(cekirdek_sayisi)


def company_cekirdekleme():
    cekirdek_sayisi = int(ui.lineCompany.text())
    thread_company(cekirdek_sayisi)


def state_cekirdekleme():
    cekirdek_sayisi = int(ui.lineState.text())
    thread_state(cekirdek_sayisi)


def zipcode_cekirdekleme():
    cekirdek_sayisi = int(ui.lineZipcode.text())
    thread_zipcode(cekirdek_sayisi)

def product_cekirdekleme2():
    cekirdek_sayisi = int(ui.lineProduct_2.text())
    thread_product_oranli(cekirdek_sayisi,60)


ui.btnProduct.clicked.connect(product_cekirdekleme)
ui.btnProduct_2.clicked.connect(product_cekirdekleme2)
ui.btnIssue.clicked.connect(issue_cekirdekleme)
ui.btnCompany.clicked.connect(company_cekirdekleme)
ui.btnState.clicked.connect(state_cekirdekleme)
ui.BtnZipcode.clicked.connect(zipcode_cekirdekleme)

sys.exit(uygulama.exec_())
