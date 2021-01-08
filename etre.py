import os 
import sys 
from colorama import *

def gereken_verilerin_alımı():
    global verilerin_olduğu_dosya, karakter, sayı, en_az_kaç_karakter, en_fazla_kaç_karakter, wordlist, sayıx
    verilerin_olduğu_dosya = str(input('verilerin olduğu dosya =>'))
    karakter = str(input('kelimelerin sonuna karakter istiyor  musunuz(istiyorsanız evet yazın)=>'))
    sayıx = str(input('kelimelerin sonuna sayı koymak istiyor musunuz(istiyorsanız evet yazın)=>'))
    wordlist = input('wordlist adı =>')

def wordlist_oluştur(dosya, wordlist):
    dosya = open(dosya, 'r')
    liste = []
    for bilgi in dosya:
        liste.append(bilgi)
        liste.append(bilgi.lower())
        liste.append(bilgi.upper())
        liste.append(bilgi.capitalize())
    wordlist = open(wordlist, 'w')
    for bilgi in liste:
        wordlist.write(bilgi+'\n')
    for bilgi1 in liste:
        for bilgi2 in liste:
            wordlist.write(bilgi1+bilgi2+'\n')
    if(karakter == 'evet'):
        for bilgi in liste:
            wordlist.write(bilgi+'#'+'\n')
            wordlist.write(bilgi+'$'+'\n')
            wordlist.write(bilgi+'!'+'\n')
        for bilgi1 in liste:
            for bilgi2 in liste:
                wordlist.write(bilgi+'#'+'\n')
                wordlist.write(bilgi+'$'+'\n')
                wordlist.write(bilgi+'!'+'\n')
    else:
        pass
    if(sayıx == 'evet'):
        for sayı in range(3000):
            for bilgi in liste:
                sayı = str(sayı)
                wordlist.write(bilgi+sayı+'\n')
                wordlist.write(sayı+bilgi+'\n')
        for sayı in range(3000):
            for bilgi1 in liste:
                for bilgi2 in liste:
                    sayı = str(sayı)
                    wordlist.write(bilgi1+bilgi2+sayı)
    else:
        pass
    dosya.close()
    wordlist.close()
gereken_verilerin_alımı()
wordlist_oluştur(dosya=verilerin_olduğu_dosya, wordlist=wordlist)