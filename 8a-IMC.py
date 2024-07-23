# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:28:23 2017

@author: andre
"""
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