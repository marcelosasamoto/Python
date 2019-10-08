'''
   ordenação por flutuação ou bolha, percorre o vetor diversas vezes e a cada passagem fazer
   flutuar para o topo o maior elemento da sequencia. 
   melhor caso n 
   pior caso n^2.
   Esse algoritmo possui contador de passos    
'''
import random, time
class BublleSort(object):
    def __init__(self):
        self.step = 0
    def bubbleSort(self, array):
        count = 0
        #print("array is currently",array)
        for idx in range(len(array)-1):
            if array[idx] > array[idx + 1]:
                array[idx],array[idx + 1] = array[idx + 1],array[idx]
                self.step += 1
                self.step += 1
                count += 1
                self.step += 1
                #print("swaped and count is currently",count)
                #print("array is currently",array)
            self.step += 1
        self.step += 1
        
        if count == 0:
            #print("Count is zero")
            #print("array is currently",array)
            self.step += 1
            return array
        else:
            #print("Count is not zero")
            self.step += 1
            return self.bubbleSort(array)
    def gerar(self,tam):
        arr = []
        for x in range(tam):
            arr.append(random.randint(0,1000))
            self.step += 1
        self.step += 1
        return arr
tam = int(input("Digite o tamanho da lista:"))
b = BublleSort()
a=b.gerar(tam)

start = time.time()
t = b.bubbleSort(a)
print("--- %s seconds ---" % (time.time() - start))
print("Passos:",b.step)
#print(a,"\n",t) #mostrar vetores