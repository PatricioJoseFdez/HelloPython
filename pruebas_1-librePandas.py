#ejemplo base
#x = 1
#if x == 1:
#    print("x es 1.")

#Estructura:series = pd.series(data, index=index)


#realMadridPlayers = pd.Series(['Keylor','Carvajal','Ramos','Nacho','Marcelo','Casemiro','Kross','Modric','Isco','Bale','CR','Asensio'], index=[0,1,2,3,4,5,6,7,8,9,10,11])
#print ("Real de Madrid: \n%s" % realMadridPlayers)

#llamamos a la librerias
import pandas as pd
import numpy as np
#CARGA DE LOS DATOS DE USERS
#creo una lista con la cabecera del txt users
userHearder = ['user_id', 'gender', 'age', 'ocupation', 'zip']
#creo un dataframe y cargo los datos
df_users = pd.read_table('C:/Users/Patricio/Documents/pruebas_1/users.txt', engine='python', sep='::', header=None, names=userHearder)
#CARGA DE DATOS DE RATINGS
#creo una lista con la cabecera del rating.txt
ratingHearder = ['user_id', 'movie_id', 'rating', 'timestamp']
#creo un dataframe y cargo los datos del rating.txt
df_ratings = pd.read_table('C:/Users/Patricio/Documents/pruebas_1/ratings.txt', engine='python', sep='::', header=None, names=ratingHearder)
#CARGA DE DATOS DE MOVIES
#creo una lista con la cabecera del movies.txt
movieHearder = ['movie_id', 'title', 'genders']
#creo un dataframe y cargo los datos del movies.txt
df_movies = pd.read_table('C:/Users/Patricio/Documents/pruebas_1/movies.txt', engine='python', sep='::', header=None, names=movieHearder)

#merge data users + ratings + movies by user_id and movie_id
merger_ratings = pd.merge(pd.merge(df_users, df_ratings), df_movies)

#Clonar el dataframe
def cloneDF(df):
    return pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy()).convert_objects(convert_numeric=True)

#agrupamos y ordenamos 
#numberRatings = cloneDF(merger_ratings)
#numberRatings = numberRatings.groupby('title').size().sort_values(ascending=False)

#avgRatings = cloneDF(merger_ratings)
#avgRatings = avgRatings.groupby(['movie_id', 'title']).mean()
#print 5 first users
#print('los 5 primeros usuarios son: \n%s' %df_users[:5])

#print('# Merge de las tablas usuarios y ratios por el user_id \n%s' % merger_ratings_users[:10])

#mostramos las 5 peliculas mas votadas
#print ('Las peliculas con más votos son: \n%s' % numberRatings[:10])

#mostrar las 5 peliculas por nota media
#print ('Avg ratings: \n%s' %avgRatings['rating'][:10])

#ejemplo de pivote simple
df_1 = cloneDF(merger_ratings)
df_1 = df_1.pivot_table(index=['movie_id', 'title'], values=['rating', 'age'])

print('columnas(movie_id + title to INDEX: \n%s' %df_1[:10])