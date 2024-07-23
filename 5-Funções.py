# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:43:56 2016

@author: andre
"""

# A definição de uma função é dada pela instrução "def" seguida do nome da função. 
# Logo depois, especificamos dentro de parênteses os parâmetros que a função deve receber

# Definindo uma função que subtrai dois números e imprime o resultado na tela
def subtrai(num1, num2):
    print num1-num2
    
# Chamando a função "subtrai"
subtrai(10,6)

# Agora definindo uma funão que subtrai e só devolve o resultado, ou seja, não o imprime na tela
def subtrai2(num1, num2):
    return(num1-num2)
    
# Definindo o valor de um parãmetro de uma função na própria definição da função
def repetir(qtd, caractere='a'):
   return(qtd*caractere)

# Chamando a função "repetir" e fornecendo os parametros "qtd" e "caractere" para ela
print repetir(3,"b")

# Chamando a função "repetir" e fornecendo SOMENTE O PRIMEIRO parametro. 
# O segundo será o "a" que está na definição da função.
print repetir(5)

# Chamando a função "repetir" e especificando os parâmetros e seus valores, NA 
# MESMA ORDEM em que foram definidos na função.
print repetir(qtd=20,caractere='*')

# Definindo uma função mais complexa
def compara_absolutos(a,b):
    "Essa função retorna se os valores absolutos de a e b são iguais"
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a == b:
        print 'Os valores absolutos de ', a, ' e ', b, ' são iguais.'
    else:
         print 'Os valores absolutos de ', a, ' e ', b, ' são diferentes.'
         
# Aqui estou chamando a função e fornecendo os valores dos parametros para ela
compara_absolutos(23,-23) 

# Na função a seguir, os parãmetros "num1" e "num2" são definidos quando chamo a função. 
# Já as variáveis "a" e "b" estão DENTRO DA FUNÇÂO, então são VARIÀVEIS LOCAIS
def multiplica(num1, num2):
    a = num1
    b = num2
    return a*b

#Chamando a funçao "multiplica"
print multiplica(2,4)


###############################################################################

# AGORA DIFERENCIANDO VARIÀVEIS LOCAIS (Aquelas que sso estao dentro das funçoes) DE GLOBAIS

###############################################################################


# No exemplo a seguir, "comida" é DEFINIDA FORA DA FUNÇÂO, então É UMA VARIÁVEL GLOBAL
comida = 'arroz' # Defino a variável global
print comida # Printo o valor da variável global
def qual_a_comida(): # Defino a função, a qual não possui nenhum parâmetro
    print 'A comida é',comida # A função usa como parâmetro de entrada o valor da variável global "comida" 
qual_a_comida() # Chamo a função e não forneço nenhum parãmetro para ela

print "******** AGORA FAZENDO NOVAS ANÀLISES *****"

def muda_comida_fake():
    comida = 'batata' # Esta variável "comida" dentro da função é uma variável LOCAL!!!
    print("Comida: {nova_comida}".format(nova_comida=comida)) # Aqui dentro da função eu estou usando a 
                                                              # variável "comida" LOCAL, e não a global!
    
print comida # Printando na tela o valor da variável global "comida" antes de mudá-la

muda_comida_fake() # Chamando a função que MUDARIA o valor da variável global "comida", porém não muda!
                   # Ela somente printa o valor da variável LOCAL, que no caso é "batata"

print 'A variável GLOBAL continua sendo', comida # Printando a variável GLOBAL

# OBS: A variável "comida" fora da função e a variável "comida" dentro da função são coisas diferentes!!!
# OBS2: Variáveis locais (aquelas dentro de funções) não afetam e nao mudam variáveis globais, mesmo que 
# os nomes sejam iguais.
# Para alterarmos uma variável global usando uma função, devemos usar a palavra "global" na frente da 
# variável que está dentro da função. Veja o exemplo abaixo:
comida = 'Arroz'

def muda_comida_global():
    global comida # Aqui aviso à função que queremos a variável GLOBAL, e não que ela crie uma variável 
                  # local
    comida = 'batata 2'
    print 'Comida: {nova_comida}'.format(nova_comida=comida)
    
print 'Antes de chamar a função, a comida é:', comida

muda_comida_global() # Chamando a função

print 'Depois de chamar a função que muda o valor da variável global, a comida mudou para:', comida

# *** RECURSIVIDADE: A função chama ela mesma dentro dela ****
def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n*fatorial(n-1)
print '5! = ', fatorial(5)