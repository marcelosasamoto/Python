"""
     Merge sort é uma ordenação por comparação do tipo dividir para conquistar.
    Sua ideia basica consiste em dividir o problema em varios subproblemas e resolver esses subproblemas atraves da recursividade.
    melhor caso n log n
    pior caso n log n
    Esse algoritmo possui contador de passos
"""
import random, time
class Mergesort(object):
    def __init__(self):
        self.step = 0

    def _split(self, array):
        self.step += 1
        return (array[: len(array) // 2], array[len(array) // 2 :])
    def _merge(self, left, right):
        esquerdoI = 0
        direitoI = 0
        result = []
        while esquerdoI < len(left) and direitoI < len(right):
            self.step += 1
            if left[esquerdoI] <= right[direitoI]:
                self.step += 1
                result.append(left[esquerdoI])
                self.step += 1
                esquerdoI += 1
                self.step += 1
            else:
                self.step += 1
                result.append(right[direitoI])
                self.step += 1
                direitoI += 1
                self.step += 1

        if esquerdoI < len(left):
            self.step += 1
            result.extend(left[esquerdoI:])
            self.step += 1
        elif direitoI < len(right):
            self.step += 1
            result.extend(right[direitoI:])
            self.step += 1
        return result
        
    def mergeSort(self, arr):
        if arr is None:
            self.step += 1
            return None
        if len(arr) < 2:
            self.step += 1
            return arr
        left, right = self._split(arr)
        self.step += 1
        self.step += 1
        return self._merge(self.mergeSort(left), self.mergeSort(right))

    def gera(self,tam):
        arr = []
        for i in range(tam):
            arr.append(random.randint(0,1000))
            self.step += 1
        self.step += 1
        return arr

m = Mergesort()
nums = m.gera(int(input("Digite o tamanho da lista:")))
start = time.time()
t = m.mergeSort(nums)
print("--- %s seconds ---" % (time.time() - start))
print("Passos:",m.step)
#print(a,"\n",t) #mostrar os vetores
