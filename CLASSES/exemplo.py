class Pessoa:
    def __init__(self,V1,V2):
        self.nome=V1
        self.idade=V2

    def setNome(self, V):
        self.nome=V

    def setIdade(self,V):
        self.idade=V

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
    