import json
import re

# RODRIGO QUINTANA - DIVISION H - TURNO NOCHE


def leer_archivo(nombre_archivo: str) -> list:
    """
    Esta función lee un archivo JSON y devuelve una lista de jugadores.

    Args: El parámetro "nombre_archivo" es una cadena que representa el nombre del
    archivo que se leerá
        nombre_archivo : str

    Returns: una lista de jugadores (jugadores) leída de un archivo JSON especificado por el parámetro
    de entrada "nombre_archivo".
    """
    lista = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        jugador = json.load(archivo)
        lista = jugador["jugadores"]

    return lista


def imprimir_menu():
    """
    Esta función imprime un menú con 21 opciones y una opción de salida.
    """
    menu = "\n1 - Mostrar la lista de todos los jugadores del Dream Team\n2 - Seleccionar indice y mostrar jugador\n3 - Guardar jugador mostrado en la opcion 2\n4 - Buscar jugador y mostrar logros\n5 - Mostrar promedio de puntos por partido del Dream Team de forma ascendente\n6 - Buscar jugador y ver si pertenece al Salon de la Fama del Baloncesto\n7 - Mostar jugador con la mayor cantidad de rebotes totales\n8 - Mostrar jugador con el mayor porcentaje de tiros de campo\n9 - Mostrar jugador con la mayor cantidad de asistencias totales\n10 - Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\n11 - Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n12 - Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor\n13 - Mostrar el jugador con la mayor cantidad de robos totales.\n14 - Mostrar el jugador con la mayor cantidad de bloqueos totales.\n15 - Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\n16 - Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido\n17 - Mostrar el jugador con la mayor cantidad de logros obtenidos.\n18 - Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n19 - Mostrar el jugador con la mayor cantidad de temporadas jugadas.\n20 - Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n23 - Crear archivo csv con el ranking de jugadores.\n24 - Determinar la cantidad de jugadores que hay por cada posición\n25 - Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente\n26 - Determinar qué jugador tiene las mejores estadísticas en cada valor.\n27 - Determinar qué jugador tiene las mejores estadísticas de todos.\n0 - Salir"
    print(menu)


def validar_opcion() -> int:
    """
    Esta función valida la opción de entrada de un usuario comprobando si coincide con una expresión
    regular y devuelve el valor entero de la opción o -1 si no coincide.

    Returns: Si la entrada del usuario coincide con el patrón de expresión regular, se devuelve un valor
    entero de la entrada. Si la entrada no coincide con el patrón, se devuelve -1.
    """
    imprimir_menu()

    while True:
        ingresar_opcion = input("\nIngrese una opción: ")

        if re.match(r"^(?:[0-9]|1[0-9]|20|2[3-7])$", ingresar_opcion):
            return int(ingresar_opcion)

        else:
            return -1


def principal():
    """
    Este es un programa basado en menús que permite al usuario realizar varias operaciones en una lista
    de jugadores de baloncesto.
    """
    while True:
        opcion = validar_opcion()

        match (opcion):
            case 1:
                mostrar_jugadores(lista_jugadores)

            case 2:
                jugador = mostrar_jugador_indice(lista_jugadores)
            case 3:
                print("A esta funcion se debe ingresar desde la opcion 2")
            case 4:
                mostrar_logros_jugador(lista_jugadores)
            case 5:
                promedio_puntos_equipo(lista_jugadores, "promedio_puntos_por_partido")

            case 6:
                miembro_salon_de_la_fama(lista_jugadores)
            case 7:
                calcular_maximo(lista_jugadores, "rebotes_totales")
            case 8:
                calcular_maximo(lista_jugadores, "porcentaje_tiros_de_campo")
            case 9:
                calcular_maximo(lista_jugadores, "asistencias_totales")
            case 10:
                mayor_que_el_valor(lista_jugadores, "promedio_puntos_por_partido")
            case 11:
                mayor_que_el_valor(lista_jugadores, "promedio_rebotes_por_partido")
            case 12:
                mayor_que_el_valor(lista_jugadores, "promedio_asistencias_por_partido")
            case 13:
                calcular_maximo(lista_jugadores, "robos_totales")
            case 14:
                calcular_maximo(lista_jugadores, "bloqueos_totales")
            case 15:
                mayor_que_el_valor(lista_jugadores, "porcentaje_tiros_libres")
            case 16:
                promedio_puntos_por_partido(lista_jugadores)
            case 17:
                mas_logros_obtenidos(lista_jugadores)
            case 18:
                mayor_que_el_valor(lista_jugadores, "porcentaje_tiros_triples")
            case 19:
                calcular_maximo_temporadas(lista_jugadores, "temporadas")
            case 20:
                mayor_que_el_valor_por_posicion(
                    lista_jugadores, "porcentaje_tiros_de_campo"
                )
            case 23:
                guardar_jugadores_en_csv(lista_jugadores, archivo_csv)
            case 24:
                contar_jugadores_por_posicion(lista_jugadores)
            case 25:
                ordenar_por_all_star(lista_jugadores)
            case 26:
                calcular_mejores_estadisticas(lista_jugadores)
            case 27:
                calcular_mejor_jugador(lista_jugadores)
            case 0:
                break


# 1
def mostrar_jugadores(lista_jugadores: list) -> str:
    """
    La función "mostrar_jugadores" toma una lista de jugadores e imprime sus nombres y posiciones.

    Args: Una lista de diccionarios que representan a los jugadores del Dream Team,
    donde cada diccionario contiene las claves "nombre" (nombre) y "posición" (posición)
        lista_jugadores: list
    """
    for jugador in lista_jugadores:
        print("{0} - {1}".format(jugador["nombre"], jugador["posicion"]))


# 2
def mostrar_jugador_indice(lista_jugadores: list) -> str:
    """
    Esta función muestra una lista de jugadores y sus estadísticas, permite al usuario seleccionar un
    jugador para verlo en detalle y ofrece la opción de guardar los datos del jugador en un archivo CSV.

    Args: lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
        lista_jugadores: list

    Returns: Falso (si el usuario elige no guardar los datos en un archivo csv) o nada (si el usuario
    elige guardar los datos en un archivo csv).
    """
    for i in range(len(lista_jugadores)):
        print("{0} - {1}".format(i, lista_jugadores[i]["nombre"]))

    ingresar_indice = int(input("Ingresar indice del jugador a mostrar: "))

    jugador_elegido = lista_jugadores[ingresar_indice]

    print(
        "\nNombre: {0}\nPosicion: {1}".format(
            jugador_elegido["nombre"], jugador_elegido["posicion"]
        )
    )
    for estadistica, valor in jugador_elegido["estadisticas"].items():
        estadisticas = quitar_guiones_bajos(estadistica)

        print("{0}: {1}".format(estadisticas.capitalize(), valor))

    pregunta_guardar_archivo = input(
        "\nDesea guardar los datos en un archivo csv? (si/no): "
    )

    if pregunta_guardar_archivo == "si":
        guardar_archivo(jugador_elegido)
    elif pregunta_guardar_archivo == "no":
        return jugador_elegido
    else:
        print("Opcion incorrecta")


def quitar_guiones_bajos(palabra: str) -> str:
    """
    La función toma una cadena con guiones bajos y devuelve la misma cadena con espacios en lugar de
    guiones bajos.

    Args: Una cadena que contiene guiones bajos que deben eliminarse
        palabra: str

    Returns: una cadena con los guiones bajos reemplazados por espacios.
    """
    palabras = palabra.split("_")
    palabras_sin_guiones = " ".join(palabras)
    return palabras_sin_guiones


# 3
def guardar_archivo(jugador_elegido: dict) -> str:
    """
    Esta función guarda un diccionario de la información de un jugador elegido en un archivo CSV.

    Args: Un diccionario que contiene información sobre un jugador elegido, incluido
    su nombre, posición y estadísticas
        jugador_elegido: dict
    """
    nombre_archivo_csv = (
        r"C:\Users\Rodrigo\Documents\PROGRAMACIÓN_I\Primer_Parcial\{0}.csv".format(
            jugador_elegido["nombre"]
        )
    )
    with open(nombre_archivo_csv, "w") as archivo:
        linea = "Nombre: {0}\nPosicion: {1}".format(
            jugador_elegido["nombre"], jugador_elegido["posicion"]
        )
        archivo.write(linea)
        for estadistica, valor in jugador_elegido["estadisticas"].items():
            estadisticas = quitar_guiones_bajos(estadistica)

            archivo.write("\n{0}: {1}".format(estadisticas.capitalize(), valor))

    print("Archivo CSV creado exitosamente.")


# 4
def mostrar_logros_jugador(lista_jugadores: list) -> str:
    """
    La función toma una lista de jugadores y solicita al usuario que ingrese el nombre de un jugador,
    luego muestra el nombre y los logros del jugador.

    Args: una lista de diccionarios que representan a los jugadores y sus logros. Cada
    diccionario contiene las claves "nombre" (nombre del jugador) y "logros" (lista de logros del
    jugador)
        lista_jugadores: list
    """
    ingresar_nombre = input("Ingrese el nombre del jugador: ")

    for jugador in lista_jugadores:
        if ingresar_nombre.lower() in jugador["nombre"].lower():
            print("\nNombre: {0}\nLogros:".format(jugador["nombre"]))
            for logro in jugador["logros"]:
                print(logro)


# 5
def ordenar_lista(lista_jugadores: list, dato: str) -> list:
    """
    Esta función ordena una lista de jugadores por una estadística determinada y devuelve la lista
    ordenada.

    Args: una lista de diccionarios que representan a los jugadores y sus estadísticas
        lista_jugadores: list

    Args: El parámetro "dato" es una cadena que representa la estadística para la cual la función
    calculará el promedio de puntos por equipo. Se utiliza para acceder al valor correspondiente en el
    diccionario "estadisticas" de cada jugador en la lista "lista_jugadores"
        dato: str

    Return: una lista ordenada de jugadores basada en sus estadísticas para un tipo de datos
    determinado (especificado por el parámetro `dato`). La lista está ordenada en orden ascendente, y el
    jugador con el valor estadístico más bajo aparece primero en la lista.
    """
    rango = len(lista_jugadores)
    flag = True

    while flag:
        flag = False
        rango = rango - 1

        for i in range(rango):
            if (
                lista_jugadores[i]["estadisticas"][dato]
                > lista_jugadores[i + 1]["estadisticas"][dato]
            ):
                lista_jugadores[i], lista_jugadores[i + 1] = (
                    lista_jugadores[i + 1],
                    lista_jugadores[i],
                )
                flag = True

    return lista_jugadores


# 5
def promedio_puntos_equipo(lista_jugadores: list, dato: str) -> str:
    lista_ordenada = ordenar_lista(lista_jugadores, "promedio_puntos_por_partido")

    for jugador in lista_ordenada:
        print(
            "{0} - {1}".format(
                jugador["nombre"],
                jugador["estadisticas"][dato],
            )
        )


# 6
def miembro_salon_de_la_fama(lista_jugadores: list) -> bool:
    """
    La función comprueba si un jugador de baloncesto determinado es miembro del Salón de la Fama del
    Baloncesto buscando en una lista de jugadores y sus logros.

    Args: una lista de diccionarios que representan a jugadores de baloncesto, donde
    cada diccionario contiene el nombre del jugador y una lista de sus logros
        lista_jugadores: list

    Returns: un valor booleano que indica si el nombre del jugador ingresado es miembro del Salón de la
    Fama del Baloncesto o no.
    """
    ingresar_nombre = input("Ingrese el nombre del jugador: ")

    for jugador in lista_jugadores:
        if ingresar_nombre.lower() in jugador["nombre"].lower():
            for logro in jugador["logros"]:
                if re.search(r"Miembro del Salon de la Fama del Baloncesto", logro):
                    print("Pertenece al Salon de la Fama del Baloncesto")
                    return True
    print("No pertenece al Salon de la Fama del Baloncesto")
    return False


# 7 - 8 - 9 - 13 - 14 
def calcular_maximo(lista_jugadores: list, dato: str) -> dict:
    """
    La función calcula el jugador con el valor más alto para una estadística dada en una lista de
    jugadores y devuelve un diccionario con la información del jugador.

    Args: Una lista de diccionarios que representan a diferentes jugadores y sus
    estadísticas
        lista_jugadores: list

    Args: dato es un parámetro de cadena que representa la estadística específica para la que
    queremos encontrar el valor máximo en la lista de jugadores. Se utiliza para acceder al valor
    correspondiente en el diccionario de estadísticas de cada jugador
         dato: str

    Returns: un diccionario que contiene el jugador con el valor más alto para la estadística dada
    (especificado por el parámetro "dato") entre la lista de jugadores (especificado por el parámetro
    "lista_jugadores").
    """
    dato_maximo = 0
    jugador_maximo = None
    flag = False
    for jugador in lista_jugadores:
        if not flag:
            dato_maximo = jugador["estadisticas"][dato]
            jugador_maximo = jugador
            flag = True
        elif jugador["estadisticas"][dato] > dato_maximo:
            dato_maximo = jugador["estadisticas"][dato]
            jugador_maximo = jugador

    dato_normalizado = quitar_guiones_bajos(dato)
    print(
        "Jugador con más {0}: {1} con {2}".format(
            dato_normalizado,
            jugador_maximo["nombre"],
            jugador_maximo["estadisticas"][dato],
        )
    )
    return jugador_maximo


# 10 - 11 - 12 - 15 - 18
def mayor_que_el_valor(lista_jugadores: list, dato: str) -> str:
    """
    Esta función toma una lista de jugadores y una estadística, solicita al usuario que ingrese un valor
    y luego imprime los nombres de los jugadores cuya estadística es mayor que el valor ingresado.

    Args: una lista de diccionarios que representan a los jugadores y sus estadísticas
        lista_jugadores: list

    Args: El parámetro "dato" es una cadena que representa una estadística de un jugador, como
    "puntos" (puntos), "rebotes" (rebotes) o "asistencias" (asistencias)
        dato: str
    """
    ingresar_valor = int(input("Ingresar un valor: "))
    print("Jugadores con más {0} que el promedio".format(quitar_guiones_bajos(dato)))
    for jugador in lista_jugadores:
        if ingresar_valor < jugador["estadisticas"][dato]:
            print("{0} - {1}".format(jugador["nombre"], jugador["estadisticas"][dato]))


# 16
def calcular_minimo(lista_jugadores: list, dato: str) -> list:
    """
    La función calcula el valor mínimo de una estadística dada para una lista de jugadores y elimina al
    jugador con el valor mínimo de la lista.

    Args: Una lista de diccionarios que representan a los jugadores y sus estadísticas
        lista_jugadores: list

    Args: El parámetro "dato" es una cadena que representa la estadística para la que queremos
    encontrar el valor mínimo en la lista de jugadores
        dato: str

    Returns: la lista actualizada de jugadores después de eliminar al jugador con el valor mínimo para
    la estadística dada (especificado por el parámetro "dato").
    """
    dato_minimo = 0
    jugador_minimo = None
    flag = False
    for jugador in lista_jugadores:
        if not flag:
            dato_minimo = jugador["estadisticas"][dato]
            jugador_minimo = jugador
            flag = True
        elif jugador["estadisticas"][dato] < dato_minimo:
            dato_minimo = jugador["estadisticas"][dato]
            jugador_minimo = jugador

    lista_jugadores.remove(jugador_minimo)

    return lista_jugadores


# 16
def promedio_puntos_por_partido(lista_jugadores: list) -> str:
    """
    Esta función calcula el promedio de puntos por juego para una lista de jugadores, excluyendo al
    jugador con el promedio más bajo.

    Args: Una lista de diccionarios que representan a los jugadores de baloncesto y
    sus estadísticas. Cada diccionario debe tener una clave "estadisticas" que contiene un diccionario
    de las estadísticas del jugador, incluyendo su "promedio_puntos_por_partido" (promedio de puntos por
    partido)
        lista_jugadores: list
    """
    lista_sin_el_peor = calcular_minimo(lista_jugadores, "promedio_puntos_por_partido")
    suma = 0
    for jugador in lista_sin_el_peor:
        suma += jugador["estadisticas"]["promedio_puntos_por_partido"]

    promedio = suma / len(lista_sin_el_peor)

    print(
        "Promedio de puntos por partido del Dream Team sin el peor: {0}".format(
            promedio
        )
    )


# 17
def mas_logros_obtenidos(lista_jugadores: list) -> dict:
    """
    La función encuentra al jugador con más logros en una lista de jugadores y devuelve su información.

    Args: Una lista de diccionarios que representan a los jugadores, donde cada
    diccionario contiene información sobre los logros de un jugador
        lista_jugadores: list
    """
    dato_maximo = 0
    jugador_maximo = None
    flag = False

    for jugador in lista_jugadores:
        contador_logros = len(jugador["logros"])
        if not flag:
            dato_maximo = contador_logros
            jugador_maximo = jugador
            flag = True
        elif contador_logros > dato_maximo:
            dato_maximo = contador_logros
            jugador_maximo = jugador

    print(
        "\nNombre: {0}\nPosicion: {1}".format(
            jugador_maximo["nombre"], jugador_maximo["posicion"]
        )
    )
    for estadistica, valor in jugador_maximo["estadisticas"].items():
        estadisticas = quitar_guiones_bajos(estadistica)

        print("{0}: {1}".format(estadisticas.capitalize(), valor))

    return jugador_maximo

#19
def calcular_maximo_temporadas(lista_jugadores: list, dato: str) -> list:
    """
    La función calcula los dos jugadores con el valor más alto para una estadística dada en una lista de
    jugadores y devuelve una lista de diccionarios con la información de los jugadores.

    Args:
        lista_jugadores: Una lista de diccionarios que representan a diferentes jugadores y sus estadísticas.
        dato: Un parámetro de cadena que representa la estadística específica para la que queremos encontrar
              el valor máximo en la lista de jugadores. Se utiliza para acceder al valor correspondiente en
              el diccionario de estadísticas de cada jugador.

    Returns:
        Una lista de diccionarios que contiene los dos jugadores con el valor más alto para la estadística dada
        (especificada por el parámetro "dato") entre la lista de jugadores (especificada por el parámetro
        "lista_jugadores").
    """
    jugadores_maximos = []
    datos_maximos = [0, 0] 
    for jugador in lista_jugadores:
        dato_actual = jugador["estadisticas"][dato]
        if dato_actual > datos_maximos[0]:
            datos_maximos = [dato_actual, datos_maximos[0]]
            jugadores_maximos = [jugador]
        elif dato_actual > datos_maximos[1]:
            datos_maximos[1] = dato_actual
            jugadores_maximos.append(jugador)

    dato_normalizado = quitar_guiones_bajos(dato)
    for  jugador in jugadores_maximos:
        print("Jugador  con más {0}: {1} con {2}".format(
            
            dato_normalizado,
            jugador["nombre"],
            jugador["estadisticas"][dato]
        ))

    return jugadores_maximos

# 20
def mayor_que_el_valor_por_posicion(lista_jugadores: list, dato: str) -> str:
    """
    Esta función toma una lista de jugadores y una estadística, solicita al usuario que ingrese un valor
    y luego imprime los nombres, posiciones y porcentajes de tiros de campo de los jugadores cuya
    estadística especificada es mayor que el valor ingresado.

    Args: Una lista de diccionarios que representan a jugadores de baloncesto, donde
    cada diccionario contiene información sobre un jugador, como su nombre, posición y estadísticas
        lista_jugadores: list

    Args: El parámetro "dato" es una cadena que representa una estadística de jugadores de
    baloncesto, como "puntos" (puntos), "rebotes" (rebotes) o "asistencias" (asistencias)
        dato: str
    """
    ingresar_valor = int(input("Ingresar un valor: "))
    print("Jugadores con más {0} que el promedio".format(quitar_guiones_bajos(dato)))

    posiciones = ["Base", "Escolta", "Alero", "Ala-Pivot", "Pivot"]

    for posicion in posiciones:
        for jugador in lista_jugadores:
            if jugador["posicion"] == posicion:
                if jugador["estadisticas"][dato] > ingresar_valor:
                    print(
                        jugador["nombre"],
                        jugador["posicion"],
                        jugador["estadisticas"]["porcentaje_tiros_de_campo"],
                    )


# 23
def guardar_jugadores_en_csv(lista_jugadores, archivo_csv):
    """
    Esta función toma una lista de jugadores y sus estadísticas, los clasifica según su desempeño en
    diferentes categorías y guarda las clasificaciones en un archivo CSV.

    Args:
        lista_jugadores: Una lista de diccionarios, donde cada diccionario representa un jugador y sus estadísticas
        archivo_csv: El nombre del archivo CSV donde se guardarán las clasificaciones
    """

    estadisticas = lista_jugadores[0]["estadisticas"].keys()

    ranking = {}
    for palabra in estadisticas:
        ordenar_lista(lista_jugadores, palabra)

        posicion = 1
        for jugador in lista_jugadores:
            nombre = jugador["nombre"]
            if nombre not in ranking:
                ranking[nombre] = {}
            ranking[nombre][palabra] = posicion
            posicion += 1

    with open(archivo_csv, "w") as archivo:
        encabezado = [
            "Jugador",
            "Puntos",
            "Rebotes",
            "Asistencias",
            "Robos",
            "Bloqueos",
        ]
        max_len_nombre = 0
        for jugador in lista_jugadores:
            nombre_len = len(jugador["nombre"])
            if nombre_len > max_len_nombre:
                max_len_nombre = nombre_len
                
        linea_encabezado = "".join(["-" * (max_len_nombre + 2)] + ["-" * 14] * len(encabezado)) 
        archivo.write(linea_encabezado + "\n")
        
        encabezado_format = "| {0:<{1}} ".format(encabezado[0], max_len_nombre)
        for columna in encabezado[1:]:
            encabezado_format += "| {0:<13} ".format(columna)
        encabezado_format += "|"
        archivo.write(encabezado_format + "\n")
        
        archivo.write(linea_encabezado + "\n")

        for jugador, estadisticas in ranking.items():
            linea_jugador = "| {0:<{1}} ".format(jugador, max_len_nombre)

            for key in [
                "puntos_totales",
                "rebotes_totales",
                "asistencias_totales",
                "robos_totales",
                "bloqueos_totales",
            ]:
                if key in estadisticas:
                    valor = str(estadisticas[key])
                    linea_jugador += "| {0:<13} ".format(valor)
                else:
                    linea_jugador += " " + "-" + " " * 11 + "|"

            linea_jugador += "\n"
            archivo.write(linea_jugador)


nombre_archivo = r"C:\Users\Rodrigo\Documents\PROGRAMACIÓN_I\Primer_Parcial\dt.json"
lista_jugadores = leer_archivo(nombre_archivo)
archivo_csv = r"C:\Users\Rodrigo\Documents\PROGRAMACIÓN_I\Primer_Parcial\dt.csv"