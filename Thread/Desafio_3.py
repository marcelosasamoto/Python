from threading import Thread
import tkinter as tk
import random
import time

aleatorio = [random.randint(0,400) for _ in range(200)]

class Tela:
    def __init__(self, windows):
        self.time = 5
        self.runing =True
        self.x = time.time()
        self.timeBT = 1
        self.count = 0
        self.windows = windows
        self.labeltext = tk.Label(windows,text=str("Tempo:%i"%self.time),width=7, height=1)
        self.labeltext.place(x=5,y=5)
        self.label = tk.Button(windows, text="Contador:0",command=self.contbutton)
        self.label.pack()
        

    def count_timer(self):
        while(self.time > 0):
            time.sleep(1)
            self.time -= 1
            self.labeltext.configure(text=str("Tempo:%i"%self.time))
        self.runing = False
        tk.Label(self.windows,text="FINALIZANDO THREADS",height=45).pack()
        time.sleep(1)
        window.quit()

    def contbutton(self):
        self.count +=1
        self.timeBT-= 0.1
        
    def refresh_button(self):
        while self.x-time.time() < self.timeBT:
            if self.runing:
                time.sleep(self.timeBT)
                self.label.configure(text="Contador:%i" % self.count)
                self.label.place(x=random.choice(aleatorio),y=random.choice(aleatorio))
                self.x = time.time()
                self.refresh_button()
            else:
                break

        
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Desafio 3")
    window.geometry("500x500")
    timer = Tela(window)
    thread1 = Thread(target=timer.count_timer)
    thread2 = Thread(target=timer.refresh_button)
    thread1.start()
    thread2.start()
    window.mainloop() 
