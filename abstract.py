from abc import ABC, abstractmethod 
import random, os

# referencia em https://www.geeksforgeeks.org/abstract-classes-in-python/
#OBS programa sem tratamento de erro, portanto nao zoa a entrada.
#classe pai
class Abstrata(ABC): 
    def __init__(self, A, B):
        for i in range(0, len(A)): #converte os elementos da lista para inteiro ex: ["1","2"] para [1,2]
            A[i] = int (A[i])
        for i in range(len(B)):     #aqui tambem
            B[i] = int (B[i])
        self.A = A
        self.B = B
    def operacoes(self):    # metodo abstato
        pass

#classe filha
class Uniao(Abstrata):
    def operacoes(self):    # sobrescrita do metodo
        A = set(self.A)     # o self.A herda da classe Abstrata
        B = set(self.B)
        C = A | B
        return sorted(C)

class Intersecçao(Abstrata):
    def operacoes(self):
        A = set(self.A)
        B = set(self.B)
        C = A & B
        return (sorted(C))
class Diferença(Abstrata):
    def operacoes(self):
        A = set(self.A)
        B = set(self.B)
        C = A - B
        return (sorted(C))
class Membro(Abstrata):
    def operacoes(self,x,y):
        if y == "1":
            if(x in self.A):
                return True
            else:
                return False
        elif y == "2":
            if(x in self.B):
                return True
            else:
                return False
class Cria_Conj_Vazio(Abstrata):
    def operacoes(self,y):
        if y == "1":
            self.A.clear()
            print("Conjunto vazio!")
            return self.A
        elif y == "2":
            self.B.clear()
            print("Conjunto vazio!")
            return self.A
class Insere(Abstrata):
    def operacoes(self,x,y):
        if y =="1":
            self.A.append(x)
            print("Valor adicionado com sucesso!")
        elif y == "2":
            self.B.append(x)
            print("Valor adicionado com sucesso!")
class Remove(Abstrata):                             # sem tratamento de erro, se x nao estiver self.A ou self.B
    def operacoes(self,x,y):
        if y == "1":
            index = self.A.index(x)
            self.A.pop(index)
            print("Valor removido com sucesso!")
        elif y =="2":
            index = self.B.index(x)
            self.B.pop(index)
            print("Valor removido com sucesso!")
class Atribui(Abstrata):
    def operacoes(self):
        A = set(self.A)
        B = set(self.B)
        A = B
        return sorted(A)
class Min(Abstrata):
    def operacoes(self,y):
        if y == "1":
            return min(self.A)
        elif y == "2":
            return min(self.B)
class Max(Abstrata):
    def operacoes(self,y):
        if y == "1":
            return max(self.A)
        elif y == "2":
            return max(self.B)
class Igual(Abstrata):
    def operacoes(self):
        A = set(self.A)
        B = set(self.B)
        if(A == B):
            return True
        else:
            return False

if __name__ == '__main__':
    array_result = ""
    array_result = set(array_result)
    input_user = 0
    while(input_user != 3):
        input_user = int(input("Menu\n1)Informar valores da Array\n2)Visualizar valores\n3)Sair\n\nMenu de Operações\n4)União\n5)Interseção\n6)Diferença\n7)Membro\n8)Esvaziar conjunto\n9)Inserir\n10)Remover\n11)Atribuir\n12)Mínimo\n13)Máximo\n14)Igual\nOpção --> "))
        if(input_user == 1):
            array_one_1 = input("Digite os números para a primeira Array separado por espaço -> ")
            array_one = array_one_1.split(" ")
            array_two_1 = input("Digite os números para a segunda Array separado por espaço -> ")
            array_two = array_two_1.split(" ")
            os.system("clear")
        if(input_user == 2):
            os.system("clear")
            print(f"Array 1 --> {array_one}\nArray 2 --> {array_two}")


        if(input_user == 4):
            os.system("clear")
            u = Uniao(array_one,array_two)
            print('\t Uniao =',Uniao(array_one,array_two).operacoes())
        if(input_user == 5):
            os.system("clear")
            print(Intersecçao(array_one,array_two).operacoes())
        if(input_user == 6):
            os.system("clear")
            print(Diferença(array_one,array_two).operacoes())
        if(input_user == 7):
            os.system("clear")
            user = int(input("Digite o número desejado --> "))
            print("Resultado -> ",Membro(array_one,array_two).operacoes(user,input("Digite qual conjunto. 1 ou 2")))
        if(input_user == 8):    
            os.system("clear")
            Cria_Conj_Vazio(array_one,array_two).operacoes(input("Digite qual conjunto. 1 ou 2"))
        if(input_user == 9):
            os.system("clear")
            user_a = int(input("Digite o valor a ser inserido --> "))
            Insere(array_one,array_two).operacoes(user_a,input("Digite qual conjunto. 1 ou 2"))
        if(input_user == 10):
            os.system("clear")
            user_b = int(input("Digite o valor a ser removido --> "))
            Remove(array_one,array_two).operacoes(user_b,input("Digite qual conjunto. 1 ou 2"))
        if(input_user == 11):
            os.system("clear")
            print(Atribui(array_one,array_two).operacoes())
        if(input_user == 12):
            os.system("clear")
            print(Min(array_one,array_two).operacoes(input("Digite qual conjunto. 1 ou 2")))
        if(input_user == 13):
            os.system("clear")
            print(Max(array_one,array_two).operacoes(input("Digite qual conjunto. 1 ou 2")))
        if(input_user == 14):
            os.system("clear")
            print("Resultado --> ",Igual(array_one,array_two).operacoes())
