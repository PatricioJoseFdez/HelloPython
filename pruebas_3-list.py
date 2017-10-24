#Tipo de datos: LISTA

#lista1 = [1, 3.14, "c1", 'patry_ho.com', True]
#print ("Los elementos de la lista y el tipo de cada uno son:\n")

#for i in lista1:
 #   print("%s  -> %s" %(i, type(i)))

#Creamos una lista nueva
listaDemarcaciones = list()

#Insertarmos elementos a la lista
listaDemarcaciones.append('Portero')
listaDemarcaciones.append('Defensa')
listaDemarcaciones.append('Lateral')
listaDemarcaciones.append('MedioCentro')
listaDemarcaciones.append('Delanteros')

#guardamos en una variable el número de elementos
numeroElementos = len(listaDemarcaciones)
#print("el numero de demarcaciones son:\t%s"%numeroElementos)
#print ("las demarcaciones son:\t%s" %listaDemarcaciones)

#insertarmos un elemento nuevo a la lista
listaDemarcaciones.insert(5, 'Extremo')
#print ("añadiendo nueva demarcación: "); print (listaDemarcaciones)

#Unir dos listas
DemarcaconesClasicas = ['Arquero', 'Carrilero', 'Delentero Centro']
listaDemarcaciones.extend(DemarcaconesClasicas)
#print (listaDemarcaciones)

#Eliminar un elemento por valor o por posición
listaDemarcaciones.remove('Portero')
#print(listaDemarcaciones)
listaDemarcaciones.pop(1)
#print(listaDemarcaciones)

#buscar la posicion de la primera aparición de un valor concreto
#print(listaDemarcaciones.index('Delanteros'))

#ver el número de veces que se repite un valor
#print(listaDemarcaciones.count('Carrilero'))

#invertir el orden de la lista
#listaDemarcaciones.reverse()
#print(listaDemarcaciones)

#ejemplo de ordenación de lista del mismo tipo de dato
print("lista desordenada")
lista2 = [5,2,9,1,12,6,8,3,4,4]
print(lista2)
print("lista ordenada con valores por defecto:")
lista2.sort(reverse=False)
print(lista2)
print("lista ordenada de forma descendente: ")
lista2.sort(reverse=True)
print(lista2)