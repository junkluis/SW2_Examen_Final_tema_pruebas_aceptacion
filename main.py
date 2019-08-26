from src.Cine import *
from src.Pelicula import *


if __name__ == '__main__':

    movie_A = Pelicula( "Carrie", "Brian De Palma",  ["John Travolta", "William Katt", "Betty Buckley"], "suspenso", ["ingles", "español"], 1976, "R")
    movie_B = Pelicula( "The Adventures Of Tinti", "Steven Spielberg",  ["Jamie Bell", "Andy Serkis", "Daniel Craig"], "suspenso", ["ingles", "español"], 2011, "PG")
    movie_C = Pelicula( "The Bourne Identity ", "Brian De Palma",  ["Matt Damon", "Franka Potente", "Chris Cooper"], "accion", ["ingles"], 2002, "PG-13")
    movie_D = Pelicula( "The Great Dictator ", "Doug Liman",  ["Charlie Chaplin", "Paulette Goddard", "Jack Oakie"], "comedia", ["ingles", "esperanto"], 1940, "PG")

    lista_peliculas = [movie_A, movie_B, movie_C, movie_D]

    resultado, msj = get_pelicula_titulo(lista_peliculas, "a")
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj, error = get_pelicula_rating(lista_peliculas, ["R", "PG"])
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj, error = get_pelicula_rating(lista_peliculas, ["R", "PG", "RC1"])
    print(msj)
    print(error)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj, error = get_pelicula_rating(lista_peliculas, ["NC-17"])
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj = get_pelicula_idiomas(lista_peliculas, "español")
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj = get_pelicula_idiomas(lista_peliculas, "chino")
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj = get_pelicula_fecha_estreno(lista_peliculas, 1999, 2012 )
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj = get_pelicula_fecha_estreno(lista_peliculas)
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj = get_pelicula_fecha_estreno(lista_peliculas, 2020, 1999)
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)

    resultado, msj = get_pelicula_fecha_estreno(lista_peliculas, 2020, 2021)
    print(msj)
    for x in resultado:
        print(x)
    print("-"*20)
