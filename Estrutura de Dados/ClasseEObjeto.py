#A classe define um "molde" para seus objetos
class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome = nome

#instanciando Objetos
eu = Pessoa("David","Santos")
ele = Pessoa("Renato","Pereira")
ela = Pessoa("Alana","Carla")

print(eu.nome,ele.nome,ela.nome)