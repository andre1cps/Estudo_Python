# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:35:37 2016

@author: andre
"""
# Dando um print na tela


# Agora fazendo contas, mas sem aperecer na tela!!!
10+5 # Adição
20-11 # Subtração
30/2 # Divisão
2**3 # Exponenciação
10 % 8 # Resto da divisão inteira
120-30+2**3 # Múltiplas operações
# Fazendo uma conta em que o resultado aparece na tela
print 12+2

# Radiciação: Para a raiz n-ésima de 5, devo elevar 5 a 1/n
print 8**(1.0/3.0) # Aqui tenho a raiz cúbica de 8

# Duas variáveis inteiras (tipo "int")
ten = 10
two = 2
print ten + two

# Duas variáveis Float (Pontos flutuantes, tipo "float")
f1 = 0.98
f2 = 0.02
print f1 + f2

# Definindo e printando strings (que são coisas dentro de aspas, variáveis tipo "str")
string1 = "Isso é uma string"
print string1
string2 = "Este número 10 tbm é uma string"
print string2
string3 = 'Isso tbm é uma string'
print string3
string4="Isso é uma string com aspas dentro: 'Oi!'"
print string4
string5='It\'s friday!'
print string5
string_grande="""Vamos fazer um teste de string grande agora mesmo: esta é uma string
muito grande"""
print string_grande
pula_linha='O lema de JK era:\n"50 anos em 5"'
print pula_linha

# Formatando e manipulando strings
teste="Python" # String com a letra "P" sendo a zero
print teste[0:3] # Indicando 3 ele vai fatiar até a letra de posição 2
print teste
print teste[3] # Irá buscar somente pela letra na posição 3
print teste[-1] # O sinal negativo indica que irá na ordem inversa - de trás pra frente
print teste[0:6:2] # Começa na posição 0, acaba na 6 e escreve de 2 em 2 letras
a='Matematica'
print a[2]+a[-5]+a[-4:]# Aqui vai ser printada a palavra "tatica", onde o comando "a[-4:]" pega as últimas 4 letras 

# Usando %s (string), %d (inteiro) e %f (float) em uma string
compra='maçã'
tipo='verde'
quilos=1.576
preco=3
print 'Maria comprou %.2f quilos de %s %s e pagou %d reais.' % (quilos,compra,tipo,preco)
print 'Maria comprou {peso} quilos de {produto} {tipo} e pagou {preco} reais.'.format(peso=quilos, produto=compra, tipo=tipo, preco=preco)

# Concatenando (juntando) strings
b = 'bla'
print 10*b
frase1 = 'Olá, tudo bem?\n'
frase2 = 'Como vai você?'
frase3 = 'Me responde! '
print 3*frase1+frase3+frase2

# Métodos de strings: .nome_metodo(argumentos)
print 'Maria comprou {peso} quilos de {produto} {tipo} e pagou {preco} reais.'.format(peso=quilos, produto=compra, tipo=tipo, preco=preco) # Método "format()"
print 'oi'.capitalize() # Retorna uma cópia da string c/ o 1° caractere maiúsculo
print 'OIE'.lower() # Retorna uma cópia da string com todos os caracteres minusculos
print 'oie'.upper() # Retorna cópia da string com todos os caracteres maiusculos

# Recebendo uma string do usuário
nome = raw_input('Digite o seu nome: ') # Este comando recebe uma string como entrada a partir do teclado
print nome
print len(nome) # O comando "len(string)" fornece o n° de caracteres da string 'nome'
sobrenome = raw_input('Agora digite seu sobrenome: ')
sobrenome = ' '+sobrenome # Aqui estou adicionando um espaço antes do sobrenome
print nome+sobrenome
idade = input('Digite sua idade: ') # Este comando recebe int ou float como entrada do teclado
altura = input('Digite a sua altura "com pontos!": ')
print type(nome) # Este comando mostra o tipo de variável inserida pelo usuário
print type(idade)
print type(altura)

# Outro tipo de tipo de variável: Booleana (tipo "bool")
Booleanaverdadeiro = True
print Booleanaverdadeiro
Bool2 = False
print Bool2

# Comando para saber qual é o tipo de certa variável: type(nome_da-variável)
print(type(Bool2))

# Convertendo variavel de um tipo em outro
# Aqui defino a variavel tipo int, que é a savings. A tipo float é a results
savings = 100
result = 100 * (1.10 ** 7)
# Para printar corretamente devo convertê-las para tipo string, colocando "str() na frente delas"
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")