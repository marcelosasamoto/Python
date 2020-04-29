from threading import Thread, Lock
import time

status = [ "VERDE", "VERMELHO"]
lock = Lock()
class Semaforo:
    def __init__(self,nome):
        self.nome = nome

    def Semaforo1(self,nome):
        global status

        print("Inicio da thread",nome)
        if(status[0] == "VERDE"):
            print(status)
            time.sleep(0.3)
            status[0] = "AMARELO"
            print(status)
            time.sleep(0.2)
            status[0] = "VERMELHO"
            status[1] =  "VERDE"
            print(status)
            time.sleep(0.5)
        elif(status[0] == "VERMELHO"):
            print(status)
            time.sleep(0.5)
            status[0] = "AMARELO"
            print(status)
            time.sleep(0.2)
            status[0] = "VERDE"
            status[0] = "VERMELHO"
            print(status)
            time.sleep(0.3)
        elif (status[0] == "AMARELO"):
            print(status)
            time.sleep(0.2)
            status[0] = "VERMELHO"
            print(status)
            time.sleep(0.5)
            status[0] = "AMARELO"
            print(status)
            time.sleep(0.3)
        print('Fim da thread ',nome)

    def Semaforo2(self,nome):
        global status
        print("Inicio da thread",nome)
        if(status[1] == "VERDE"):
            print(status)
            time.sleep(0.3)
            status[1] = "AMARELO"
            print(status)
            time.sleep(0.2)
            status[1] = "VERMELHO"
            status[0] = "VERDE"
            print(status)
            time.sleep(0.5)
        elif(status[1] == "VERMELHO"):
            time.sleep(0.5)
            print(status)
            status[1] = "VERDE"
            time.sleep(0.3)
            print(status)
            status[1] = "AMARELO"
            time.sleep(0.2)
            print(status)
        elif (status[1] == "AMARELO"):
            print(status)
            time.sleep(0.2)
            status[1] = "VERMELHO"
            print(status)
            time.sleep(0.5)
            status[1] = "AMARELO"
            print(status)
            time.sleep(0.3)
        print('Fim da thread ',nome)

def mostrar():
    while True:
        print(status)
thr1 = list()
thr2 = list()
Nvidas_da_threads = 3
sem1 = 'VERDE'
sem2 = 'VERMELHO'


sema1 = (Semaforo(("Semaforo 1")))
sema2 = (Semaforo(("Semaforo 2")))

for i in range(Nvidas_da_threads):
    thr1.append(Thread(target=sema1.Semaforo1,args=[sema1.nome]))
    thr2.append(Thread(target=sema2.Semaforo2,args=[sema2.nome]))


for i in range(Nvidas_da_threads):
    thr1[i].start()
    thr1[i].join()
    thr2[i].start()
    thr2[i].join()
