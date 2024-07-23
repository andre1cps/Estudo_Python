# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:23:21 2016

@author: andre
"""

# DEFININDO UMA CLASSE, QUE É UMA "MOLDE" DE QUALQUER COISA
# Definimos um objeto carro e esse objeto tem métodos (ações) e atributos (características).
# Nesse caso, um carro pode ter um método Ligar(), Acelerar(), Freiar(), Trocar_Marcha(), Desligar(), etc. Tudo isso são ações que um carro poderia fazer.
# Além disso, um carro pode ter atributos como Cor, Quantidade_de_Lugares, Velocidade_Maxima, etc. Essas são características que podem variar dependendo do carro.

# Uma classe tem um nome, vários métodos (que são funções específicas daquela classe) e vários atributos (variáveis internas à um método específico)
class Carro: # Criando a classe "Carro"
    def _init_(self): # Este método ou função ESPECIAL (CONSTRUTOR) é executado sempre que que quero criar um novo objeto da classe
        self.cor = "Preto"
        self.quantidade_de_lugares = 7
        self.velocidade_maxima = 200
        self.ligado = False
        self.marcha = 1
        self.velocidade = 0
carro = Carro() # Aqui estou criando um objeto que será um Carro, ou seja, que terá as mesmas características e ações que a classe "Carro" tem
carro.cor = 'Vermelho' # Mudadndo um dos atributos do objeto "carro"
carro.velocidade_maxima = 250 # Mudadndo outro atributo do objeto "carro"
# Verificando o status de um atributo do objeto carro:
print carro.cor
# OBS: Nossa classe "Carro" continua sendo um molde com os valores que passamos quando a definimos! Aqui só alteramos o atributo "cor" do objeto "carro"
# Agora vamos criar uma outra classe de carro com mais algumas funcionalidades:
class Carro2: 
    def _init_(self): # Este método ou função ESPECIAL (CONSTRUTOR) é executado sempre que que quero criar um novo objeto da classe
        self.cor = "Preto"
        self.quantidade_de_lugares = 7
        self.velocidade_maxima = 200
        self.ligado = False
        self.marcha = 1
        self.velocidade = 0
    def ligar(self):
        self.ligado = True
        
    def acelerar(self, nova_veloc):
        self.velocidade = nova_veloc
        
    def freiar(self):
        self.velocidade -= 10
        
    def trocar_marcha(self, nova_marcha):
        self.marcha = nova_marcha
    
    def desligar(self):
        self.ligado = False
# Notar que todos os métodos devem receber "self" para indicar que estamos trabalhando com o objeto em si.
# Chamando um método (que é uma função interna à classe) assim:
carro2 = Carro2()
carro2.ligar()
print carro2.ligado
carro2.trocar_marcha(2)
print carro2.marcha
carro2.acelerar(200)
print carro2.velocidade
carro2.desligar()
print carro2.ligado



# Criando uma nova classe QUE HERDA atributos de outra classe já existente 
class Gol(Carro2): # Esta classe "Gol" vai herdar tudo igualzinho da classe "Carro2"
    def __init__(self):
       # Carro2.__init__(self) # Chamando o construtor de Carro2 para a classe Gol herdar as características de Carro2
        self.cor = "Prata" # Editamos (modificamos) alguns atributos da nova classe
        self.quantidade_de_lugares = 5
        self.ar_condicionado_ligado = False

    def ligar_ar_condicionado(self): # Adicionando um novo método à nova classe
        self.ar_condicionado_ligado = True

    def ligar(self): # Reescrevendo a função ou método "ligar"
        self.ligado = True
        self.marcha = 6
        
gol = Gol()
gol.ligar()
print gol.ligado
print gol.marcha
