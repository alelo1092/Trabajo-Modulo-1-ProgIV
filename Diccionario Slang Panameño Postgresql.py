# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:25:11 2021

"""

import sqlite3

#Creamos la base de datos
conn = sqlite3.connect('DiccionarioSlangPanameño.db')


c = conn.cursor()

#Creamos la tabla que contiene las palabras del diccionario
c.execute("""CREATE TABLE if not exists Palabras (
            Palabra text primary key,
            Significado text
            )""")
conn.commit()


#Definimos las funciones que aplicaran los requerimientos del programa

def insertar(a,b):
    c.execute("insert into Palabras(Palabra, Significado) VALUES (?,?)", (a,b))
    conn.commit()

def eliminar(PalabraE):
    sentencia = "delete from Palabras WHERE Palabra = " + "'" + PalabraE + "'"
    c.execute(sentencia)
    conn.commit()

def mostrarDatos():
    c.execute("SELECT Palabra, Significado from Palabras")
    rows = c.fetchall()
    for row in rows:
        print("\nPalabra= ", row[0], "Significado = ", row[1])

def significadopalabra(palabrasig):
    sentencias = "select Palabra, Significado from Palabras WHERE Palabra = " + "'" + palabrasig + "'"       
    c.execute(sentencias)
    rows = c.fetchall()
    for row in rows:
        print("El significado de la palabra", row[0],"es : ", row[1])

def editarSignificado(PalabraV,SignificadoN):
    sentencia = "UPDATE Palabras SET Significado =" +"'" + SignificadoN + "'" "WHERE Palabra =" + "'" + PalabraV + "'"
    c.execute(sentencia)
    conn.commit()


#Una vez definidas todas las funciones le damos inicio al programa con un bucle While


print("Inicio del Programa Diccionario Slang Panameño")

while True:
    Respuesta1 = input("Si desea agregar una Palabra al Diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta1 == "1":
        Respuesta11 = "1"
        while Respuesta11 == "1":
            a=input("Introduzca la Palabra : ")
            b = input ("Introduzca su significado : ")
            insertar(a,b)
            Respuesta11= input("Deseas agregar otra palabra?, Si (1), No (2)")
            
    Respuesta2 = input("\nSi desea editar el significado de una palabra del Diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta2 == "1":
        PalabraV = input("Introduzca la palabra que desee cambiarle el significado : ")
        SignificadoN = input("Introduzca el nuevo significado de la palabra anterior : ")
        editarSignificado(PalabraV,SignificadoN)

    Respuesta3 = input("\nSi desea ver todas los datos del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta3 == "1":
        mostrarDatos()
        
    Respuesta4 = input("\nSi desea ver todas los datos del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta4 == "1":
        mostrarDatos()
        
    Respuesta5 = input("\nSi desea ver algun significado de una palabra del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta5 == "1":
        palabrasig= input("\nIntroduzca la palabra que quiere saber su significado : ")
        significadopalabra(palabrasig)
        
    Respuesta6 = input("\nSi desea eliminar alguna palabra del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta6 == "1":
        PalabraE = input("\nIntroduzca la palabra que desea eliminar : ")
        eliminar(PalabraE)
    
    Respuesta7 = input("\nSi desea salir del programa presione 1, de lo contrario presione otro valor : ")
    if Respuesta6 == "1":
        break
    
print("Fin del Programa")

conn.close()
