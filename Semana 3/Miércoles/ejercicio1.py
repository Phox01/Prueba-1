#Diccionario
currency_dict={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency=input('Escribe una moneda: Euro, Dollar o Yen \n')
print(currency_dict.get(currency,'Moneda no encontrada'))