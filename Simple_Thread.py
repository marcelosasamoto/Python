import threading, queue
import Desafo_1 as desafio  #Importa a Classe

programa = desafio.Program()
programa.gerarLetras()

fila_espera = queue.Queue()

# O programa.(Nome da funcao) para ser o alvo da thread
threadzin1 = threading.Thread(target=programa.contVogal)
threadzin2 = threading.Thread(target=programa.contConsoante)      
threadzin3 = threading.Thread(target=programa.ordenarAlfabeto,args=[programa.letras,fila_espera])    

# Inicia a thread
threadzin1.start()
threadzin2.start()
threadzin3.start()

threadzin3.join()

x = fila_espera.get()
print("Fim da thread ordenar",x,'\n\n\n')
programa.mostrar()

