"""
El proposito de este programa es imprimir una lista que muestra los diputados ganadores por departamento
Uso: python main.py <departamento>
"""
import sys
from csv import reader
from pandas import *
from operator import itemgetter
from diputados import Diputados

diputados_departamentos = []
candidatos_list = []
arg = ""

if (len(sys.argv) > 1):
    argumentos = sys.argv[1:]
    for argumento in argumentos:
        arg = arg + argumento.upper() + " "
else:
    print("Uso python main.py <departamento>")
arg = arg.strip()

with open('departamentos.txt', 'r') as file:
    departamentos = reader(file, delimiter=',')
    for departamento in departamentos:
        diputados_departamentos.append(departamento)

with open('candidatos.txt', 'r') as file:
    candidatos = reader(file, delimiter='\t')
    for candidato in candidatos:
        candidatos_list.append(candidato)

for i in range(0, len(candidatos_list)):
    candidatos_list[i][2] = int(candidatos_list[i][2])
    candidatos_list[i][4] = int(candidatos_list[i][4])

for i in range(0, len(diputados_departamentos)):
    diputados_departamentos[i][2] = int(diputados_departamentos[i][2])

candidatos_list_sorted = sorted(candidatos_list, key=itemgetter(1, 4), reverse=True)
   
if (any(arg == e[0] for e in diputados_departamentos)):
    diputados = Diputados(candidatos_list_sorted, diputados_departamentos)
    print(DataFrame(diputados.getDiputadosDepartamento(arg), columns=['Departamento', 'Partido', 'Casilla', 'Nombre', 'Marcas']))
else:
    print("No existe ese departamento")