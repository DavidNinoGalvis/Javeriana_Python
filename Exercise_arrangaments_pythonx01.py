#!/usr/bin/env python


"""
introduction to programming - Marco Antonio Nino
Student: David Nino Galvis   / 18/09/2022    
"""
def isPrime(number):
    """This function define if a number is prime

    Args:
        number ({int}): Define the number to evaluate

    Returns:
        {bool}: True = Prime - False = Number isn't prime
    """
    if number < 2:
        return False
    for i in range (2, number):
        if number % i == 0:
            return False
    return True
#print(isPrime(7))


def drawDiagonal(number):
    """print diagonal amount

    Args:
        number ({int}): amount the characters
    """
    p = "."
    for n in range(number):
        cad = ""
        for i in range(n):
            if i < n-1:
                cad += "."
            else:
                cad += chr(92) #print character #92 (Code ASCII)
        print(cad)          
#drawDiagonal(10)


def primeList(number):
    """Store in a list the {number} count primes

    Args:
        number ({int}): top limit - numbers to evaluate

    Returns:
        {int}: arrangements with primes numbers
    """
    lista = []
    for i1 in range(1,number+1):
        contador = 0
        for i2 in range(1,i1+1):
            if i1 % i2 == 0:
                contador += 1 # Dividers amount
        if contador == 2 :
            lista.append(i1) # add value to arrangement
    return lista
#print(primeList(20))


def foodMachine(input_money):
    """function to return money from a vending machine
    Args:
        input_money ({int}): money deposited in the machine

    Returns:
        {int}: arrangements with back money
    """
    if input_money < 0: # if {input_money} is low 0 , return -1
        return -1
    nominaciones = [100, 200, 500, 1000] # currencies allowed
    coins_to_return = [0, 0, 0, 0]
    moneda_mil = input_money // nominaciones[3]
    coins_to_return[3] = moneda_mil
    resto1 = input_money % nominaciones[3]
    if resto1 > 0: # if there is a remainder, go to the next coin
        moneda_quinientos = resto1 // nominaciones[2]
        coins_to_return[2] = moneda_quinientos
        resto2 = resto1 % nominaciones[2]
        if resto2 >0: # if there is a remainder, go to the next coin
            moneda_docientos = resto2 // nominaciones[1]
            coins_to_return[1] = moneda_docientos
            resto3 = resto2 % nominaciones[1]
            if resto3 > 0: # if there is a remainder, go to the next coin
                moneda_cien = resto3 // nominaciones[0]
                coins_to_return[0] = moneda_cien
                resto4 = input_money % nominaciones[0]
    return coins_to_return
#print(foodMachine(3500))
