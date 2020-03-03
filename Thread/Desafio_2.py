import threading, random, queue, time

tamanho = 40
tabuleiro = [list() for s in range(tamanho)]                   # O vetor é compartilhado com as threads

class Player:
    def __init__(self,nome):
        self.nome = nome
        self.dinheiro = 0.0
        self.posicao = 0
        self.livre = True
        self.qt = 0
    def jogar_dado(self):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        print(self.nome,"tirou", dado1, "e",dado2)
        #time.sleep(0.1)
        self.qt = self.qt + 1
        return dado1, dado2

    def dado_repetido(self,dados):
        #print(self.nome,"jogou ",dados)
        if self.livre == True and dados[0] == dados[1]:
            self.livre = False                                  # O Player fica preso
            #print(self.nome,"Ficou preso")
            x = self.jogar_dado()
            #print(self.nome,"jogou",x)
            self.dado_repetido(x)
            #self.jogar_dado()
        elif self.livre == False and dados[0] != dados[1]:
                                                                #print("ainda esta preso")
            x = self.jogar_dado()
            self.dado_repetido(x)
        elif self.livre == False and dados[0] == dados[1]:
            self.livre = True                                   # O player fica livre
            #print(self.nome,"pode continuar...")
            #self.jogar_dado()
        elif self.livre == True and dados[0] != dados[1]:
            if self.posicao+dados[0]+dados[1] >=100:
                self.posicao = 100
            else:
                self.posicao = self.posicao + dados[0] + dados[1]
                if self.posicao % 2 == 0:
                    #print("Par")
                    self.dinheiro = self.dinheiro + 79.99
                else:
                    #print("impar")
                    self.dinheiro = self.dinheiro + 53.21
                #print("posicao",self.posicao)

def multiplay(player,mais_rapido):
    start_time = time.time()
    running = True
    while running:
        player.dado_repetido(player.jogar_dado())
        #print(player.nome,"na posicao",player.posicao)
        for i in tabuleiro:                                      
                for j in i:
                    if player.nome == j:
                        i.remove(player.nome)                   # Area de seccao critica do vetor tabuleiro.
        if player.posicao < len(tabuleiro):                     # O vetor tabuleiro é compartilhado com as outras threads
            tabuleiro[player.posicao].append(player.nome)       # Area de seccao critica.
        else:
            tabuleiro[tamanho-1].append(player.nome)
        print(tabuleiro)
        
        if player.posicao >= len(tabuleiro):
            print(player.nome,"Chegou lá!")
            tempo_execucao = time.time() - start_time
            mais_rapido.put([player.nome,player.dinheiro,player.qt,tempo_execucao])
            break
        

p1 = Player('Ana')
p2 = Player('Tiago')
p3 = Player('Joao')
p4 = Player('Luiza')

tabuleiro[0].append(p1.nome)
tabuleiro[0].append(p2.nome)
tabuleiro[0].append(p3.nome)
tabuleiro[0].append(p4.nome)
print(tabuleiro)

# O programa.(Nome da funcao) para ser o alvo da thread

mais_rapido = queue.Queue()
thr1 = threading.Thread(target=multiplay,args=[p1,mais_rapido])
thr2 = threading.Thread(target=multiplay,args=[p2,mais_rapido])
thr3 = threading.Thread(target=multiplay,args=[p3,mais_rapido])
thr4 = threading.Thread(target=multiplay,args=[p4,mais_rapido])


thr1.start()
thr2.start()
thr3.start()
thr4.start()


thr1.join()
thr2.join()
thr3.join()
thr4.join()


x = list()
for i in range(4):
    x.append(mais_rapido.get())
rico = ['nome',0]
for i in range(len(x)):
    if x[i][1] > rico[1]:
        rico[1]= x[i][1]
        rico[0]= x[i][0]

print('\nO player mais rico é o',rico[0], "com R$", rico[1])
print('\nA ordem para o player mais rapido foi')
for i in range(len(x)):
    print(i+1,"lugar foi",x[i][0],"levou %.3fsec"%x[i][3], "com R$",x[i][1],"e tem",x[i][2],"jogadas")

