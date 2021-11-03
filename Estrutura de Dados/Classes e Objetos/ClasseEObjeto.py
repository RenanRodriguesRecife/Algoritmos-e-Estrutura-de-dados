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

# -- Encapsulamento --
#
#Controla aquilo que ficará ou não disponível aos usuários
#Garante o controle de visibilidade dos membros de uma classe
#Permite a abstração de detalhes e foco apenas naquilo que interessa
#Em geral, os atributos da classe são ocultados do usuário, os 
#quais devem ser acessados através de uma interface definida por métodos.
#
#Em Python existe dois níveis de acesso aos membros de uma classe:
#Público e Privado
#por padrão, todos os membros de uma classe em python são públicos
#os membros privados são definidos através de dois underscores à frente
#do identificador
# self.__nome
# self.__sobrenome
# def __metodoQualquer():

#OBS:
#Embora Python oferte um certo controle de visibilidade, esse não é
#tão rigoroso quanto o de outras linguagens orientadas a objetos
# Membros privados continuam podendo ser acessados por membros
#externos à classe
# Membros privados podem ser acessado fora da classe da seguinte
#forma:
# obj._NomeClasse__ID
# a._A__foo()
#• O objetivo é evitar o acesso não intencional aos membros privados



# -- Herança --
#
#versões mais especializadas de algumas classes
#Através da herança pode se derivar classes mais especializadas
#A classe principal é chamada de superclasse
#A classe derivada é chamada de subclasse

#Objetos de uma subclasse possuem todos os atributos e métodos da
#classe mãe (superclasse) e outros específicos da subclasse

#Herança

class Empregado:
    def __init__(self, nome, matricula):
        self.__nome = nome  
        self.__matricula = matricula
    
class Gerente(Empregado):
     Empregado.__init__(self,nome,matricula)
     self.gerencia = gerencia