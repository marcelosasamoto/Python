import json

    # Para rodar precisa carregar os dados do busscadata.json
    # Caso for usar outro exemplo, tem que definir o self.heuristica
class Busca:
    def __init__(self):
        self.no = {}
        self.no_pilha = {}
        self.heuristica = {}
        
    def adicionar_no(self, no):
        self.no[no] = []
    
    def adicionar_custo(self, no_inicio, no_final, custo):
        self.no[no_inicio].append([no_final,custo])

    def verifica_no_ligado(self, no_inicio, no_final):
        if no_inicio in self.no:
            for i in self.no[no_inicio]:
                if no_final == i[0]:
                    return True
        return False

    def mostrar(self):
        for i in self.no:
            print(i,":",end=" ")
            for j in self.no[i]:
                for k in j:
                    print(k,end=" ")
                print(end='\t')
            print()

    
    def carregar_dados(self):
        try:
            with open('buscadata.json') as file:
                dado = json.load(file)
                self.no = dado[0]
                self.heuristica = dado[1]
            file.close()
            print("Carregado.")
        except:
            print('Falha ao encontrar o arquivo ou decodificação')
    def salvar_dados(self):
        file = open('buscadata.json', 'wb')
        dados_cidade = json.dumps((self.no,self.heuristica))
        file.write(dados_cidade.encode())
        file.close()
        print('Foi salvo os dados.')
        
    def buscar(self, origem, destino):
        custo = 0
        cam = [origem]
        while origem != destino:
            he = int(self.heuristica[self.no[origem][0][0]])
            no=None
            c=0
            for i in self.no[origem]:
                #print(self.heuristica[i[0]])
                if he > int(self.heuristica[i[0]]):
                    he = int(self.heuristica[i[0]])
                    origem=i[0]
                    c =int(i[1])
            custo+=c
            cam.append(origem)
            print('no:',origem,'custo',c)
        print("caminho:",cam,"custo:",custo)


    def main(self):
        rodando = None
        #self.carregar_dados()
        while rodando != '0':
            rodando = input('\n0 - Sair \n1 - Add nó\n2 - Add custo\n3 - Mostrar\n4 - Buscar\n5 - Carregar Dados\n6 - Salvar Dados ')
            if rodando == '1':
                ent = input('Digite o nó: ')
                if ent not in self.no:
                    self.adicionar_no(ent)
            if rodando == '2':
                if len(self.no) > 0:
                    ent1 = input('Digite o nó inicial:')
                    ent2 = input('Digite no final:')
                    ent3 = input('Digite o custo do nó:')
                    if ent1 in self.no and ent2 in self.no and not self.verifica_no_ligado(ent1,ent2) and ent1!='' and ent2!='' and ent3!='':
                        self.adicionar_custo(ent1,ent2,ent3)
                        self.adicionar_custo(ent2,ent1,ent3)
                else:
                    print('Adicione primeiro um nó')
            if rodando == '3':
                self.mostrar()
            if rodando == '4':
                self.buscar(input('Digite o inicio: '),input("Digite o final: "))
            if rodando == '5':
                self.carregar_dados()
            if rodando == '6':
                ent  = input("Voce deseja salvar? Digite s para sim e qualquer coisa nao")
                if ent == 's':
                    self.salvar_dados()
            

busca = Busca()
busca.main()
