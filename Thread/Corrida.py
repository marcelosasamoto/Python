import threading, random, queue, time
Ncavalo = 4
tamanho = 20
pista = [list() for s in range(tamanho)]                   # O vetor é compartilhado com as threads
controller = []
lock = threading.Lock()

# FIZ A IMPLEMTACAO DE PRIORIDADE DE THREADS EM PYTHON, POIS NAO TEM IMPLEMENTACAO NATIVA. 
# OLHE O FOR E O time.sleep(), POIS É A MINHA IMPLEMENTAÇAO DE PRIORIDADE DE THREADS.
# EU DEFINIR O NUMERO DO CAVALO, COMO A PRIORIDADE DA THREAD, QUANTO MAIOR O VALOR, MAIOR PRIORIDADE (DORME MENOS)
class Cavalinho:
    def __init__(self,nome,prioridade):
        self.nome = nome
        self.posicao = 0
        self.prioridade = prioridade
    
    
def Corrida(horse,mais_rapido):
    start_time = time.time()
    t = horse.prioridade
    dormiu = 0
    block = False
    running = True
    while running:
        for i in range(t,Ncavalo):
            #print(horse.nome, dormiu,'vezes que dormiu')
            time.sleep(0.01)
            dormiu += 1
            if t == i:
                if block == False:
                    #print(horse.nome,'Liberado')
                    block = True

                    horse.posicao += 1
                    print(horse.nome,'posicao: ',horse.posicao)   # Caso queira ver a posicao do cavalo
                    for i in pista:                                      
                            for j in i:
                                if horse.nome == j:
                                    i.remove(horse.nome)                   
                    if horse.posicao < len(pista):                    
                        pista[horse.posicao].append(horse.nome)     
                    else:
                        pista[tamanho-1].append(horse.nome)
                    #print(pista)                               # Caso queria ver a corrida dos cavalos, descomenta o print()
                    
                    if horse.posicao >= len(pista):
                        print(horse.nome,"Chegou lá!")
                        tempo_execucao = time.time() - start_time
                        mais_rapido.put([horse.nome,tempo_execucao])
                        #print("--------------------------------------------Fim da Thread", horse.nome)
                        break


                    
                    break
                else: 
                    block = False
                
        horse.posicao += 1
        #print(horse.nome,'posicao: ',horse.posicao)   # Caso queira ver a posicao do cavalo
        for i in pista:                                      
                for j in i:
                    if horse.nome == j:
                        i.remove(horse.nome)                   # Area de seccao critica do vetor pista.
        if horse.posicao < len(pista):                     # O vetor pista é compartilhado com as outras threads
            pista[horse.posicao].append(horse.nome)       # Area de seccao critica.
        else:
            pista[tamanho-1].append(horse.nome)
        #print(pista)
        
        if horse.posicao >= len(pista):
            print(horse.nome,"Chegou lá!")
            tempo_execucao = time.time() - start_time
            mais_rapido.put([horse.nome,tempo_execucao])
            #print("--------------------------------------------Fim da Thread", horse.nome)
            break
    print(horse.nome,'--------------- Dormiu ',dormiu, 'vezes')


Cavalo = list()

for i in range(Ncavalo):
    Cavalo.append(Cavalinho('Cavalo '+str(i+1),i))
    pista[0].append(Cavalo[i].nome)
print(pista)
mais_rapido = queue.Queue()

thr = list()

for i in range(Ncavalo):
    thr.append(threading.Thread(target=Corrida,args=[Cavalo[i],mais_rapido]))

for i in range(Ncavalo):
    thr[i].start()
    
for i in range(Ncavalo):
    thr[i].join()
    
x = list()
for i in range(Ncavalo):
    x.append(mais_rapido.get())

    

print('\nA ordem para o horse mais rapido foi')
for i in range(len(x)):
    print(i+1,"lugar foi",x[i][0],"levou %.6fsec"%x[i][1])

