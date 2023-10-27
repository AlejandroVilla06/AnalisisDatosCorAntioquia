from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios

#Usamos la funcion crear CSVUsuarioss
crearCSVUsuarios(usuarios, 'bdUsuarios.csv')