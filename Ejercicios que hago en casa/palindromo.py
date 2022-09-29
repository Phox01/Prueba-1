##Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
#1---Crear lista con input
#2--If lista== reverso lista
##print Su palabra x es un palindromo
word = input('Escriba una palabra: ')
for lett in word:
    print(lett)
if word==word.reverse():
    j