# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:46:49 2016

@author: andre
"""

# Módulos são conjuntos de funções pré-definidas.
# Para importar um módulo, faço: "import nome_do_módulo"

# Para saber quais funções um certo módulo possui, é só escrever "help(nome-do_módulo)" no console.

# Após ter importado um módulo, qualquer função pertencente a ele pode ser 
# utilizada através do comando: "nome_do_modulo.função(argumento)".

# É possível importar só uma função de um módulo. Fazemos isso escrevendo:
# "from nome_do_modulo import função", e aquela função já estará disponível para ser cahamada.

# O módulo "math" contém muitas funções matemáticas embutidas. Já o módulo "cmath" possui funções para
# tratamento de numeros complexos. Ambos módulos retornam números em ponto flutuante, e, no caso de 
# funções trigonométricas, retorna em radianos. Para inserir o módulo math, faço:
import math

# Agora vou usar a função exponencial presente no módulo math:
print e*1


# Para definir meu próprio módulo, eu escrevo as funções que farão parte dele 
# e salvo o arquivo com a extensão .py. Aqui vai um exemplo (Cálculo de IMC):
print "Este software calcula seu índice de massa corporal (IMC) e seu peso ideal"
peso_teclado = input('Insira seu peso em quilogramas: ')
altura_teclado = input('Insira sua altura em metros (utilizando ponto no lugar de vírgula): ')
imc2 = peso_teclado/(altura_teclado**2)
print "Seu índice de massa corporal é: %.2f" % (imc2) 

def indice(peso=peso_teclado,altura=altura_teclado):
    imc = peso/(altura**2)   
    return imc
    
def estado(imc2=indice()):
    if imc2 < 24.9:
        print "Você está com o índice de massa corporal saudável."
    elif 24.9 < imc2 < 29.9:
        print "Você está com poucos quilos a mais, mas está saudável."
    elif 29.9 < imc2 < 40:
        print "Você está acima do peso, mas não é obeso."
    elif imc2 > 40:
        print "Você está obeso, por favor se cuide mais."
    else:
        print "Você está magro demais, isto pode lhe trazer problemas de saúde!"
        
def pesoideal(peso=peso_teclado,altura=altura_teclado):
    a = 20*(altura**2)
    b = 24.9*(altura**2)
    print "Seu peso ideal se encontra entre %f e %f" %(a,b)
    
indice()
estado()
pesoideal()


