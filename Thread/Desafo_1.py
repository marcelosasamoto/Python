from threading import Thread
import queue
import time, random, string

class Program:
    def __init__(self):
        self.letras = list()
        self.qtVogal = None
        self.qtConsoante = None
        self.ordenado = None

    def gerarLetras(self):
        for i in range(50):
            self.letras.append(random.choice(string.ascii_lowercase) )

    def contVogal(self):
        cont = 0
        for i in self.letras:
            time.sleep(0.1)
            print('Contando vogal...')
            if i in 'aeiou':
                cont=cont+1
        self.qtVogal = cont
        
    def contConsoante(self):
        cont = 0
        for i in self.letras:
            time.sleep(0.1)
            print('Contando consoante...')
            if not i in 'aeiou':
                cont=cont+1
        self.qtConsoante = cont

    def ordenarAlfabeto(self,ent,out_queue):
        x = list()
        for i in string.ascii_lowercase:
            for j in ent:
                if i is j:
                    x.append(j)
                print('Ordenando vetor')
                time.sleep(0.006)
        out_queue.put(x)
        self.ordenado = x

    def mostrar(self):
        print('Vetor Original')
        for i in self.letras:
            print(i,end=' ')
        print('Vetor Ordenado')
        for i in self.ordenado:
            print(i,end=' ')
        print()
        print('         Total Vogal:', self.qtVogal)
        print('         Total Consoante',self.qtConsoante)
    
    


''' Thread simples
program = Program()      
program.gerarLetras()
threadzin1 = Thread(target=program.contVogal)
threadzin2 = Thread(target=program.contConsoante)
threadzin3 = Thread(target=program.ordenarAlfabeto)

threadzin1.start()
threadzin2.start()
threadzin3.start()
'''