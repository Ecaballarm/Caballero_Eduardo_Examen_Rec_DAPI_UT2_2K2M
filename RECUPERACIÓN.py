# Ejercicio 1#
def check_DGT(ruta):
    file = open(ruta, 'r', encoding="utf-8")
    lineas = file.readlines()
    lineacorrecta = []
    for linea in lineas:
        datos = linea.split(",")
        if not datos[0] == "Nombre":
            datos[0] = datos[0].title()
            datos[1] = datos[1].title()
            datos[2] = datos[2].title()
            datos[3] = datos[3].title()

        lineacorrecta.append(datos)
        print(datos)


check_DGT("C:/Users/Eduardo/Documents/GitHub/DGT.csv")

# Ejercicio 2#
countries_dict = {'30': "Grecia", '33': "Francia", '34': "España", '351': "Portugal", '380': "Ucrania",
                  '39': "Italia", '41': "Suiza", '44': "Reino Unido", '49': "Alemania", '7': "Rusia"}
# Ejercicio 3#
nif_dict = {'0': "T", '1': "R", '2': "W", '3': "A", '4': "G",
            '5': "M", '6': "Y", '7': "F", '8': "P",
            '9': "D", '10': "X", '11': "B", '12': "N",
            '13': "J", '14': "Z", '15': "S", '16': "Q",
            '17': "V", '18': "H", '19': "L", '20': "C",
            '21': "K", '22': "E"}


# Ejercicio 4#
def check_username(user_name):
    """
    Función para corregir los nombres y apellidos y ponerlos en formato capitalizado
    :param user_name: Nombre y apellido en formato no capitalizado
    :return: Devuelve el nombre en formato capitalizado
    """
    return user_name.title()


# Ejercicio 5#
def check_nif(user_nif):
    """
    Función para corregir mediante la forma matemática la letra del NIF
    :param user_nif: NIF del usuario
    :return: Devuelve el mismo número dl NIF pero con la letra correcta
    """
    nif_numero = user_nif[0:8]
    letra_correcta = nif_dict[str(int(nif_numero) % 23)]
    return nif_numero + letra_correcta


# Ejercicio 6#
def check_phone(telefono_completo):
    """
    Función para cambier el formato de un teléfono en otro
    :param telefono_completo: Número en formato incorrecto
    :return: Número en formato correcto
    """
    numero1 = telefono_completo.split("(")
    numero2 = numero1[1].split(")")
    numero3 = numero2[1].split("-")
    formato_corecto = '+' + numero2[0] + '-' + numero3[0] + numero3[1]
    pais = countries_dict[numero2[0]]
    return pais, formato_corecto


# Ejercicio 7#
def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """
    Función que recoge todas las multas y las suma
    :param multas_radar: Valor de las multas por radar
    :param multas_ITV: Valor de las multas por ITV
    :param multas_estupefacientes: Valor de las multas por estupefacientes
    :return: Devuelve la suma de todas las multas
    """
    bill = multas_radar + multas_ITV + multas_estupefacientes
    return int(bill)
