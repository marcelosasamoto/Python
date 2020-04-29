from threading import Thread, Lock
import time, random
lock = Lock()
class Barbeiaria():
    def __init__(self):
        self.nCliente = list()
        self.BarceiroAtivo = False
        self.cadeiras = 4
        self.ClientesAtendidos = list()
        self.ClientesPerdidos = list()
    
    def tadormindo(self):
        if len(self.nCliente) == 0:
            print('Barbeiro dormindo')
            self.BarceiroAtivo = False
    def ClienteEntra(self, name):
        
        time.sleep(random.uniform(0.1,1.0))
        print('numero de cliente',len(self.nCliente),'cadeiras',self.cadeiras)
        self.tadormindo()
        if self.BarceiroAtivo:
             
             self.BarceiroAtivo = True
        else:
            if len(self.nCliente) < self.cadeiras:
                print('\tCliente',name,'chegou')
                self.nCliente.append(name)
            elif len(self.nCliente) >= self.cadeiras:
                print('Cliente',name,' vai embora')
                self.ClientesPerdidos.append(name)
            else:
                self.BarceiroAtivo = False
                print('Barbeiro dormindo')
    def Cortar(self):
        lock.acquire()
        if len(self.nCliente) > 0:

            print('\tCortando...',self.nCliente[0])
            time.sleep(random.uniform(2,3))
            if len(self.nCliente)>0:
                self.ClientesAtendidos.append(self.nCliente[0])

                print('\tProximo!',self.nCliente[0]) 
                self.nCliente.pop(0)
        lock.release()


Bar = Barbeiaria()
clientes = list()
print('numero de cliente',len(Bar.nCliente),'cadeiras',Bar.cadeiras)
print()
for i in range(5):
    clientes.append(Thread(target=Bar.ClienteEntra,args=[i+1]))
    fazercorte = (Thread(target=Bar.Cortar))
    
    clientes[i].start()
    clientes[i].join()
    fazercorte.start()
fazercorte.join()
for i in range(5,12):
    clientes.append(Thread(target=Bar.ClienteEntra,args=[i+1]))
    fazercorte = (Thread(target=Bar.Cortar))
    
    clientes[i].start()
    clientes[i].join()
    fazercorte.start()
  
fazercorte.join()
print('Clientes atendidos:',Bar.ClientesAtendidos)
print('Clientes perdidos:',Bar.ClientesPerdidos)