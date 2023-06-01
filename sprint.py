import random
import string

# generar contraseña usando random()
# debe contener : mayúsculas, minúsculas y números


def generarPassword():
    caracteres = string.ascii_letters + string.digits
    password = "".join(random.choice(caracteres) for _ in range(8))
    return password


def crearCuenta(usuario):
    password = generarPassword()
    print("Creando una cuenta para: ", usuario)
    print("La contraseña asignada es: ", password)
    telefono = input("Ingrese un número telefónico de 8 dígitos: ")
    
    # verifica que telefono tenga 8 dígitos y sólo sean números
    while len(telefono) != 8 or not telefono.isdigit():
        print('El número telefónico debe tener 8 dígitos.')
        telefono = input('Ingrese número telefónico de 8 dígitos: ')

    # -- diccionario para guardar una cuenta 
    # -- con llaves usuario, contraseña y telefono
    cuenta = {'Usuario' : usuario, 'Contraseña' : password, 'Telefono' : telefono}    
    return cuenta

usuarios = [
    'Persona 1',
    'Persona 2',
    'Persona 3',
    'Persona 4',
    'Persona 5',
    'Persona 6',
    'Persona 7',
    'Persona 8',
    'Persona 9',
    'Persona 10',
]
# -- lista vacia para guardar los usuarios con su respectiva contraseña
# -- y teléfono
cuentas = []

# -- bucle para poder iterar sobre los elementos de la lista usuarios
for usuario in usuarios:
    cuenta = crearCuenta(usuario)
    cuentas.append(cuenta)
    print('---------------')

# -- mostrar las 10 personas con su contraseña y telefono
for cuenta in cuentas:
    print('Usuario: ' , cuenta['Usuario'])
    print('Contraseña: ' , cuenta['Contraseña'])
    print('Telefono:' , cuenta['Telefono'])    
    print('---------------')


