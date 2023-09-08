#esto es una lista
dias_semana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo']

#imprimir los datos de una lista con un for
print("Días de la semana")
for día in dias_semana:
    print(día)

#esto es un diccionario de alumnos con sus calificaciones
calificaciones = {"Pepe":[2,4,5],"Juan":[3,4,4],"Yazmin":[4,3,5]}
print("Lista de alumnos")
for c in calificaciones:
    print(c)

print("Lista de alumnos con sus calificaciones")
for c in calificaciones:
    print(c,' : ' ,calificaciones[c])

print("Lista de alumnos y promedio de calificaciones")
for c in calificaciones:
    print(c)
    suma = 0
    for i in calificaciones[c]:
        suma +=i
    print('prom: {0}'.format((suma/len(calificaciones[c]))))
#tuplas, semejante a las listas pero inmutables
print('Meses del año')
meses = ('enero','febrero','marzo','abril','mayo')
for mes in meses:
    print(mes)


#otra lista, y los métodos de la lista
precios = [4500,1200,3600,8000]
print(precios)
#agregar elementos a la lista
precios.append(900)
print(precios) 
#quitar elementos según posición
precios.remove(1200)
print(precios)
#quitar el último elemento
print(precios.pop())
print(precios)       

materias = ["Matemáticas", "Fisíca","Química","Historia","Lengua"]
notas = []
#recorrer materias como materia
for materia in materias:
    calificacion = input("¿Qué notas has sacado en " + materia + "?")
    notas.append(calificacion)
for i in range(len(materias)):
    print("En " + materias[i] + "has sacado " + notas[i])   

persona = {}
continuar = True
while continuar:
    #puedes cargar cualquier dato sobre una persona en el formato clave:valor
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    #Tienes que escribir Si para continuar, en cualquier otro caso es False
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

    canasta = {}
    continuar = True
    while continuar:
        item = input('Introduce un artículo: ')
        precio = int(input('Introduce el precio de ' + item + ': '))
        canasta[item] = precio
        #para continuar se debe escribir si
        continuar = input('¿Quieres añadir artículos a la lista (si/no)? ') == "si"
    coste = 0
    print('Lista de la compra')
    for item, precio in canasta.items():
        print(item, '\t', precio)
        coste += precio
    print('Coste total: ' , coste)                   