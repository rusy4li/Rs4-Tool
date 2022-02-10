try:
    import os
except ImportError:
    print(">>> 'os' modül hatası!")
try:
    import time
except ImportError:
    print(">>> 'time' modül hatası!")

# -*- coding:utf-8 -*-
#!/usr/bin/env python

# Setup Notları:
# Python3 veya daha üst bir sürüm kurulu olması gerekiyor!
# Dosya veya klasörleri silmeyiniz lütfen!
#####


print(" request modulü indiriliyor...")
time.sleep(1)
os.system("pip install request")
os.system("cls")
##
print(">>> colorama Modulü İndiriliyor...")
time.sleep(1)
os.system("python -m pip install colorama")
os.system("cls")
##

sr = os.listdir()
if "main.py" in sr or "wordlist" in sr:
    print(" Dosyalarda hata var!")
