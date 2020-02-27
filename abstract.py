from abc import ABC, abstractmethod 
import random, os
  
class Abstrata(ABC): 
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.resultado = ""
    def operacoes(self):
        pass


class Uniao(Abstrata):
    def operacoes(self):
        A = set(self.A)
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
    def operacoes(self,x):
        if(x in self.A):
            return True
        else:
            return False
class Cria_Conj_Vazio(Abstrata):
    def operacoes(self):
        self.A.clear()
        print("Conjunto vazio!")
        return self.A
class Insere(Abstrata):
    def operacoes(self,x):
        self.A.append(x)
        print("Valor adicionado com sucesso!")
class Remove(Abstrata):
    def operacoes(self,x):
        index = self.A.index(x)
        self.A.pop(index)
        print("Valor removido com sucesso!")
class Atribui(Abstrata):
    def operacoes(self):
        A = set(self.A)
        B = set(self.B)
        A = B
        return sorted(A)
class Min(Abstrata):
    def operacoes(self):
        return min(self.A)
class Max(Abstrata):
    def operacoes(self):
        return max(self.A)
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
    abs = Abstrata(0,0)
    u = Uniao([2,3],[1,2,7])
    print(u.operacoes())
    while(input_user != 3):
        input_user = int(input("Menu\n1)Informar valores da Array\n2)Visualizar valores\n3)Sair\n\nMenu de Operações\n4)União\n5)Interseção\n6)Diferença\n7)Membro\n8)Esvaziar conjunto\n9)Inserir\n10)Remover\n11)Atribuir\n12)Mínimo\n13)Máximo\n14)Igual\nOpção --> "))
        if(input_user == 1):
            array_one_1 = input("Digite os números para a primeira Array -> ")
            array_one = array_one_1.split(" ")
            array_two_1 = input("Digite os números para a segunda Array -> ")
            array_two = array_two_1.split(" ")
            os.system("clear")
            
            #Finish here
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
            user = input("Digite o número desejado --> ")
            print("Resultado -> ",Membro(array_one,array_two).operacoes(user))
        if(input_user == 8):    
            os.system("clear")
            Cria_Conj_Vazio(array_one,array_two).operacoes()
        if(input_user == 9):
            os.system("clear")
            user_a = input("Digite o valor a ser inserido --> ")
            Insere(array_one,array_two).operacoes(user_a)
        if(input_user == 10):
            os.system("clear")
            user_b = input("Digite o valor a ser removido --> ")
            Remove(array_one,array_two).operacoes(user_b)
        if(input_user == 11):
            os.system("clear")
            print(Atribui(array_one,array_two).operacoes())
        if(input_user == 12):
            os.system("clear")
            print(Min(array_one,array_two).operacoes())
        if(input_user == 13):
            os.system("clear")
            print(Max(array_one,array_two).operacoes())
        if(input_user == 14):.
            os.system("clear")
            print("Resultado --> ",Igual(array_one,array_two).operacoes())