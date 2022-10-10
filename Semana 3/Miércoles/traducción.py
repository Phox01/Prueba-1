words={}
words_input=input('Ingrese una palabra seguida de dos puntos y su traducción, después una coma para poner otra. \nEjemplo: hola:hello\n')
for item in words_input.split(', '):
    español, ingles=item.split(':')
    words[español]=ingles
frase=input('Escribe una frase que quieras traducir: \n')
for item in frase.split():
    if item in words:
        print(words[item], end=' ')
    else:
        print(item, end=' ')
