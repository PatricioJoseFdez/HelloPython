# tipo de datos: DICCIONARIOS (key - int : value - sting)
#futbolistas_realmadrid = dict()
futbolistas_realmadrid = {
    1 : "Keylor Navas",
    2 : "Carvajal",
    5 : "Varane",
    4 : "S.Ramos",
    6 : "Nacho",
    12 : "Marcelo"
}

#recorrer un diccionario y imprimir clave-valor
for i,j in futbolistas_realmadrid.items():
    print ("%s ---> %s" %(i,j))

numJugadores = len(futbolistas_realmadrid)
print("el número total de jugadores es: %i" %numJugadores)

keys = futbolistas_realmadrid.keys()
print("las claves son: %s" %keys)
values = futbolistas_realmadrid.values()
print("los valores de las claves son: %s" %values)

elemento = futbolistas_realmadrid.get(9)
print("el futuro mejor defensa español y cuya número es es 6 es: %s" %elemento)

#elemento2 = futbolistas_realmadrid.setdefault(7,'El Bicho')
#print ("Añadimos el jugador con el 7. Si alguien tiene clave 7 no inserta: %s" %elemento2)
#numJugadores = len(futbolistas_realmadrid)
#print ("Ahora el total de jugadores es: %s" %numJugadores)

#futbolistas_realmadrid.pop(5)
#print("Varane es baja, eliminamos de la lista de convocados \n%s" %futbolistas_realmadrid)

#futbolistas_realmadridCopy = futbolistas_realmadrid.copy()
#print("la copia de los futbolista del real madrid: \n%s" %futbolistas_realmadridCopy)

#claves = ['nombre', 'apellido', 'edad', 'teléfono', 'mail']
#futbolistas_realmadridDatosPersonales = dict.fromkeys(claves, 'sindatos')
#print ("new diccionario con claves de la lista 'claves': \n%s" %futbolistas_realmadridDatosPersonales)
#print(type(futbolistas_realmadrid))
existe1 = 2 in futbolistas_realmadrid
existe2 = 8 in futbolistas_realmadrid
print("comprobación si estan convocados los jugadores 2 y 8:\n\tel jugador 2:%s\n\tel jugador 8:%s" %(existe1,existe2))

#recorrerDiccionario = futbolistas_realmadrid.items()
#print("\nPasar el diccionario a tuplas C-V: \n%s" %recorrerDiccionario)

canteranos = {
    20:'Asensio',
    17:'Lucas Vazquez',
    14:'Marcos LLorente'
}
futbolistas_realmadrid.update(canteranos)
print("la nueva lista de convocados es: \n%s" %futbolistas_realmadrid)