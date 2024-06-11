import threading
import time
from datetime import datetime

def read_multithreading_haqida():
    print(datetime.now())
    time.sleep(1)
    qator_raqam=0
    with open('multithreading.txt', 'r') as f:
        for i in range(qator_raqam+1):
            malumot=f.readline()
            if i==qator_raqam:
                print(malumot.strip())

def read_multithreading_tezlik():
    time.sleep(1)
    qator_raqami=1
    with open('multithreading.txt', 'r') as f:
        for i in range(qator_raqami+1):
            malumot=f.readline()
            if i==qator_raqami:
                print(malumot.strip())

def read_multithreading_foydalanish():
    time.sleep(1)
    qator_raqami_1=2
    with open('multithreading.txt', 'r') as f:
        for i in range(qator_raqami_1+1):
            malumot=f.readline()
            if i==qator_raqami_1:
                print(malumot.strip())

def read_multithreading_i_o():
    time.sleep(1)
    qator_raqam=3
    with open('multithreading.txt', 'r') as f:
        for i in range(qator_raqam+1):
            malumot=f.readline()
            if i==qator_raqam:
                print(malumot.strip())

def read_multithreading_gil():
    time.sleep(1)
    qator_raqami=4
    with open('multithreading.txt', 'r') as f:
        for i in range(qator_raqami+1):
            malumot=f.readline()
            if i==qator_raqami:
                print(malumot.strip())

def read_multithreading_qiyinchiliklar():
    time.sleep(1)
    qator_raqami=5
    with open('multithreading.txt', 'r') as f:
        for i in range(qator_raqami+1):
            malimot=f.readline()
            if i==qator_raqami:
                print(malimot.strip())

def read_multithreading_xulosa():
    time.sleep(1)
    qator_raqami=6
    with open('multithreading.txt', 'r') as f:
        for i in range(qator_raqami+1):
            malumot=f.readline()
            if i==qator_raqami:
                print(malumot.strip())

thred1=threading.Thread(target=read_multithreading_haqida())
thred2=threading.Thread(target=read_multithreading_tezlik())
thred3=threading.Thread(target=read_multithreading_foydalanish())
thred4=threading.Thread(target=read_multithreading_i_o())
thred5=threading.Thread(target=read_multithreading_gil())
thred6=threading.Thread(target=read_multithreading_qiyinchiliklar())
thred7=threading.Thread(target=read_multithreading_xulosa())

# thread.star()==> funksiyalarimzi ishlashini taminlaydi
thred1.start()
thred2.start()
thred3.start()
thred4.start()
thred5.start()
thred6.start()
thred7.start()
print(datetime.now())

# thread.join()==>funksiya tugagandan keyin keyingi funksiya ishlashin taminlaydi
thred1.join()
thred2.join()
thred3.join()
thred4.join()
thred5.join()
thred6.join()
thred7.join()

