
'''
 O quicksort é um metodo de ordenação muito rapido e eficiente criado por C.A.R. Hoare em 1960.
 Ele criou o quicksort ao tentar traduzir um dicionario de ingles para russo, ordenando as palavras, 
 tendo como objetivo reduzir o problema original em subproblemas que possam ser resolvidos mais facil e rapido
 Melhor caso n log n 
 Pior caso n^2
 Esse algoritmo possui contador de passos
'''
import random, time

class Quick(object):
    def __init__(self):
        self.step = 0
    def particao(self, a, ini, fim):
        pivo = a[fim-1]
        self.step += 1
        start = ini
        self.step += 1
        end = ini
        self.step += 1
        for i in range(ini, fim):
            self.step += 1
            if a[i] > pivo:
                self.step += 1
                end += 1
                self.step += 1
            else:
                self.step += 1
                end += 1     
                self.step += 1  
                start += 1
                self.step += 1
                a[i], a[start-1] = a[start-1], a[i]
                self.step += 1
        self.step += 1
        return start-1
        
    def quickSort(self, a, ini, fim):
        #print(a)
        if ini < fim:
            self.step += 1
            pp = self.randparticao(a, ini, fim)
            self.step += 1
            self.quickSort(a, ini, pp)
            self.step += 1
            self.quickSort(a, pp+1,fim)
            self.step += 1
        return a
        
    def randparticao(self,a,ini,fim):
        self.step +=1
        rand = random.randrange(ini,fim)
        self.step += 1
        a[rand], a[fim-1] = a[fim-1], a[rand]
        self.step += 1
        self.step += 1
        return self.particao(a,ini,fim)
    def gerarlista(self,tam):
        lista = []
        for x in range(tam):
            lista.append(random.randrange(0,1000))
            self.step += 1
        self.step += 1
        return lista


q = Quick()
tam = int(input("Digite o tamanho da lista:"))
a = q.gerarlista(tam)
start = time.time()
t = q.quickSort(a,0,len(a))
print("--- %s seconds ---" % (time.time() - start))
print("Passos:",q.step)
#print(a,"\n",t) #mostrar os vetores