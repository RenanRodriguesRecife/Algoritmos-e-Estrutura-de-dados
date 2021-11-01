#A classe define um "molde" para seus objetos
class Pessoa:
    #O método especial __init__ é um construtor
    #tem como objetivo definir e inicializar os valores
    #dos atributos do objeto
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome = nome
#O self é um parametro especial que referência para o 
#próprio objeto

#destrutor em python se chama __del__
#destrutores são métodos especiais que são
#chamados quando o objeto deixa de existir
    def __del__(self):
        del self.nome
        del self.sobrenome
        print("Apagado")

#para apagar um objeto
a = Pessoa("carlos","silva")
b = a 
del a

#ALguns outros métodos interessantes são:
# __str__ -- usado para definir como o objeto deve ser impresso (e.g. com o print a)
# __repr__ -- usado para definir como o objeto deve ser exibido
# __lt__ -- comparação, operador <
# __gt__ -- comparação, operador >
# __eq__ -- comparação, operador ==



#instanciando Objetos
eu = Pessoa("David","Santos")
ele = Pessoa("Renato","Pereira")
ela = Pessoa("Alana","Carla")

print(eu.nome,ele.nome,ela.nome)


#A programação orientada a objeto está
#fundamentada em 3 princípios fundamentais:
#encapsulamento, herança e polimorfismo