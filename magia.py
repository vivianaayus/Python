#-*-coding:utf-8 -*-
# Diccionario de cada mes con su respectivo número y nombre
Calendario= {'1':'Enero', '2':'Febrero', '3':'Marzo', '4':'Abril',
             '5': 'Mayo', '6':'Junio', '7':'Julio', '8':'Agosto',
             '9':'Septiembre', '10':'Octubre', '10':'Octubre',
             '11': 'Noviembre', '12':'Diciembre'}


# Instrucciones para la entrada
print chr(27)+"[0;36m"+"A su mes de nacimiento multipliquelo por 2"

print "A la respuesta sumele 5"

print "Ahora multiplique la respuesta anterior por 50"

print "Y finalmente sumele su EDAD \n"

# Pide la respuesta de los calculos al jugador
rta = raw_input("Dame tu respuesta final... Y la magia estará hecha")

# Convertir a entero
rta1 = int(rta)

# Convierte el resultado de la resta en un string
final = str(rta1 - 250)

cadena = final

# Decisión para resultados con 3 o 4 cifras.
if len(cadena) == 4:
 mes = (cadena[0:2])
 mesf = Calendario.get(mes, 'X')
 edad = (cadena[2:4])
else:
 mes = (cadena[0])
 mesf = Calendario.get(mes, 'X')
 edad = (cadena[1:3])

#Imprime el resultado
print chr(27)+"[0;35m"+"JA el mes de nacimiento es:"
print (mesf)

print chr(27)+"[0;32m"+"Y tu edad es:"
print(edad)
