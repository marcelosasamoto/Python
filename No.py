class No:
    def __init__(self,no_atual):
        self.no_atual = no_atual
        self.proximo_no = list()
    def adicionarCusto(self, proximo_no, custo):
        self.proximo_no.append([proximo_no,custo])
