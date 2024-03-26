# Definicion de variables

nombre = "Pedro"
edad = 15
materia = "Nuevas Tecnologias"
nota1 = 4.0
nota2 = 4.5
result = (nota1 + nota2) / 2
dia = 0
semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

if(result > 3.0):
    print("Ganaste la materia: " + materia)
else:
    print("Perdiste la materia: " + materia)   
    
    
while dia < 7:
    print("Hoy es " + semana[dia])
    dia +=1    