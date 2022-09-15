import random
import time
# Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
RESET = '\033[39m'
# puntaje
score = random.randint(0, 10)
while True:
    start = input(
        RED + "Digite 'si' para  iniciar la trivia, 'no' para finalizar: \n" +
        RESET).lower()
    if start == "si":
        break
    elif start == "no":
        break
    else:
        print("Valor incorrecto, ingrese si o no: ")
while True:
    correctas, incorrectas = 0, 0
    if start == "si":

        print(BLUE + "Bienvenido a mi trivia sobre informatica" + RESET)
        time.sleep(0.5)
        print(BLUE + "Pondremos a prueba tus conocimientos" + RESET)
        time.sleep(0.5)
        print(BLUE + "Tienes", score, "Puntos" + RESET)
        time.sleep(0.5)
        nombre = input(GREEN + "Ingresa tu nombre: " + RESET)
        print(YELLOW + "\nBienvenido" + RESET, nombre)
        print(
            YELLOW +
            "Responde las siguientes preguntas digitando la alternativa correcta"
            + RESET)
        print(YELLOW + "'Enter' para enviar tu respuesta:\n" + RESET)
        print(BLUE + "pregunta 1:\n" + RESET)
        print(BLACK +
              "¿En qué año se desarrolló el lenguaje de programación C?\n" +
              RESET)
        print(CYAN + "a) en 1968" + RESET)
        print(CYAN + "b) en 1970" + RESET)
        print(CYAN + "c) en 1972" + RESET)
        respuesta_1 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_1 not in ("a", "b", "c", "x"):
            respuesta_1 = input(
                RED +
                "Debes responder a, b, o c. Ingresa nuevamente tu respuesta: "
                + RESET)
        if respuesta_1 == "c":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nMuy bien, C fue creado en 1972 por Dennis M. Ritchie en los Laboratorios Bell como evolución del anterior lenguaje B.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_1 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es la C, fue creado en 1972 por Dennis M. Ritchie en los Laboratorios Bell como evolución del anterior lenguaje B.\n "
                + RESET)
            score -= 5
            incorrectas += 1
            print(f"Tienes {score} puntos")
        time.sleep(1)
        print(BLUE + "\npregunta 2:" + RESET)
        print(
            BLACK +
            "\n¿Recuerdas cuál fue la contraseña para los controles informáticos durante 8 años de los misiles nucleares estadounidenses?\n"
            + RESET)
        print(CYAN + "a) 12345678" + RESET)
        print(CYAN + "b) 00000000" + RESET)
        print(CYAN + "c) qwerty1232" + RESET)
        respuesta_2 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_2 not in ("a", "b", "c", "x"):
            respuesta_2 = input(
                RED +
                "Debes responder a, b, o c. Ingresa nuevamente tu respuesta: "
                + RESET)
        if respuesta_2 == "b":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nAsí es, esta era la contraseña “súper segura” que estuvo ocho años activa y que daba acceso al control informático de las cabezas nucleares de Estados Unidos.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_2 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es la b, 00000000 era la contraseña “súper segura” que estuvo ocho años activa y que daba acceso al control informático de las cabezas nucleares de Estados Unidos.\n"
                + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        time.sleep(1)
        print(BLUE + "\npregunta 3:" + RESET)
        print(
            BLACK +
            "\nLa primera unidad de disco duro de 1 GB se anunció en 1980, pesaba alrededor de 250 kilos y costaba 40.000 dólares.\n"
            + RESET)
        print(CYAN + "a) Verdadero" + RESET)
        print(CYAN + "b) Falso" + RESET)
        respuesta_3 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_3 not in ("a", "b", "x"):
            respuesta_3 = input(
                RED +
                "Debes responder a o b. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_3 == "a":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nCorrecto, pesaba alrededor de 250 kilos y costaba 40.000 dólares\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_3 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es la 'a'.Pesaba alrededor de 250 kilos y costaba 40.000 dólares\n"
            )
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        time.sleep(1)
        print(BLUE + "\npregunta 4:" + RESET)
        print(
            BLACK +
            "\nUn medio de codificación de texto en el que cada símbolo está representado por 16 bits es...\n "
            + RESET)
        print(CYAN + "a) LZW " + RESET)
        print(CYAN + "b) ASCII " + RESET)
        print(CYAN + "c) Unicode " + RESET)
        respuesta_4 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_4 not in ("a", "b", "c", "x"):
            respuesta_4 = input(
                RED +
                "\nDebes responder a, b, o c. Ingresa nuevamente tu respuesta:\n"
                + RESET)
        if respuesta_4 == "c":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nMuy bien! Unicode es un sistema de codificación informático que tiene como objetivo unificar los intercambios de texto a nivel internacional. Cada carácter se describe con un nombre y un código que lo identifica de manera única, independientemente del medio informático o el software utilizado.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_4 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es la c, Unicode es un sistema de codificación informático que tiene como objetivo unificar los intercambios de texto a nivel internacional. Cada carácter se describe con un nombre y un código que lo identifica de manera única, independientemente del medio informático o el software utilizado.\n"
                + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 5:" + RESET)
        print(BLACK + "\n¿Qué significa Wi-Fi?\n" + RESET)
        print(CYAN + "a) Wiggly Fibres" + RESET)
        print(CYAN + "b) Wireless Fidelity" + RESET)
        print(CYAN + "c) Wireless Fings" + RESET)
        respuesta_5 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_5 not in ("a", "b", "c", "x"):
            respuesta_5 = input(
                RED +
                "Debes responder a, b, o c. Ingresa nuevamente tu respuesta: "
                + RESET)
        if respuesta_5 == "b":
            score += 10
            correctas += 1
            print(GREEN + "\nLa respuesta es correcta\n" + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_5 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(RED + "\nIncorrecto" + RESET, nombre,
                  GREEN + "la respuesta es la Wireless Fidelity" + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 6:" + RESET)
        print(BLACK +
              "\n¿Recuerdas cuál fue el primer navegador de la historia?\n" +
              RESET)
        print(CYAN + "a) Netscape Navigator" + RESET)
        print(CYAN + "b) Internet Explorer" + RESET)
        print(CYAN + "c) World Wide Web" + RESET)
        respuesta_6 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_6 not in ("a", "b", "c", "x"):
            respuesta_6 = input(
                RED +
                "Debes responder a, b, o c. Ingresa nuevamente tu respuesta: "
                + RESET)
        if respuesta_6 == "c":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nCorrecto! Se llamaba igual que la red. Introducido el 26 de febrero de 1991, el científico británico Tim Berners-Lee presentó WorldWideWeb que corría bajo plataforma NexTSTEP. Posteriormente fue rebautizado a NEXUS para evitar la confusión con la propia World Wide Web.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_6 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es la c, World Wide Web, se llamaba igual que la red, introducido el 26 de febrero de 1991, el científico británico Tim Berners-Lee presentó WorldWideWeb que corría bajo plataforma NexTSTEP. Posteriormente fue rebautizado a NEXUS para evitar la confusión con la propia World Wide Web.\n"
                + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 7:" + RESET)
        print(
            BLACK +
            "\nLa misma persona que alquiló su garaje a Larry Page y Sergei Brin para crear Google terminó convirtiéndose en CEO de Youtube.\n"
            + RESET)
        print(CYAN + "a) Verdadero" + RESET)
        print(CYAN + "b) Falso" + RESET)
        respuesta_7 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_7 not in ("a", "b", "x"):
            respuesta_7 = input(
                RED +
                "Debes responder a, b, o c. Ingresa nuevamente tu respuesta: "
                + RESET)
        if respuesta_7 == "a":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\n¡Verdadero! Se trata de Susan Wojcicki, directora ejecutiva de YouTube.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_7 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es Verdadero, Se trata de Susan Wojcicki, directora ejecutiva de YouTube.\n"
                + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)

        print(BLUE + "\npregunta 8:" + RESET)
        print(
            BLACK +
            "\n¿Qué sustancia se coloca en la parte externa del procesador para evitar que se sobrecaliente durante su funcionamiento?\n"
            + RESET)
        print(CYAN + "a) Pasta térmica" + RESET)
        print(CYAN + "b) Soluto de yodo" + RESET)
        print(CYAN + "c) Nitrógeno líquido" + RESET)
        respuesta_8 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_8 not in ("a", "b", "c", "x"):
            respuesta_8 = input(
                RED +
                "Debes responder a, b, o c. Ingresa nuevamente tu respuesta: "
                + RESET)
        if respuesta_8 == "a":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nExcelente! La pasta térmica, sirve como elemento físico intermediario entre la cpu y el disipador.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_8 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(RED + "\nIncorrecto" + RESET, nombre)
            print(
                GREEN +
                "\nLa respuesta es la a. La pasta térmica, sirve como elemento físico intermediario entre la cpu y el disipador.\n"
                + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 9:" + RESET)
        print(BLACK + "\n¿Y qué significa Mhz?\n" + RESET)
        print(CYAN + "a) Millihercios" + RESET)
        print(CYAN + "b) Macrohercicos" + RESET)
        print(CYAN + "c) Megahercios" + RESET)
        respuesta_9 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_9 not in ("a", "b", "c", "x"):
            respuesta_9 = input(
                RED +
                "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_9 == "c":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nMuy bien! Un megahercio es una unidad de medida de la frecuencia, equivale a 10⁶ herciosa.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_9 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(RED + "\nIncorrecto" + RESET, nombre)
            print(
                GREEN +
                "\nLa respuesta es la c. Un megahercio es una unidad de medida de la frecuencia, equivale a 10⁶ hercios.\n"
                + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)

        print(BLUE + "\npregunta 10:" + RESET)
        print(
            BLACK +
            "\nTYPEWRITER es la palabra en inglés más larga que podemos escribir usando las letras de una única fila del teclado.\n"
            + RESET)
        print(CYAN + "a) Verdadero" + RESET)
        print(CYAN + "b) Falso" + RESET)
        respuesta_10 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_10 not in ("a", "b", "x"):
            respuesta_10 = input(
                RED +
                "Debes responder a o b. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_10 == "a":
            score += 10
            correctas += 1
            print(GREEN +
                  "\nLa respuesta correcta es: Verdadero. ¡Sorpresa!\n" +
                  RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_10 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(RED + "\nIncorrecto" + RESET, nombre)
            print(GREEN + "\nLa respuesta es Verdadero\n" + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 11:" + RESET)
        print(
            BLACK +
            "\n¿A quién le debemos el diseño del primer ratón para ordenador?\n"
            + RESET)
        print(CYAN + "a) Charles Babbage" + RESET)
        print(CYAN + "b) Douglas Engelbart" + RESET)
        print(CYAN + "c) Konrad Zuse" + RESET)
        respuesta_11 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_11 not in ("a", "b", "c", "x"):
            respuesta_11 = input(
                RED +
                "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_11 == "b":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nMuy bien! Douglas Engelbart inventó el primer ratón alrededor de 1964 y estaba hecho de madera.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_11 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es la b. Douglas Engelbart inventó el primer ratón alrededor de 1964 y estaba hecho de madera.\n"
                + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 12:" + RESET)
        print(
            BLACK +
            "\nLos puntos que componen la imagen de una fotografía digital se llaman...\n"
            + RESET)
        print(CYAN + "a) Puntos de resolución" + RESET)
        print(CYAN + "b) Puntos digitales" + RESET)
        print(CYAN + "c) Pixeles" + RESET)
        respuesta_12 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_12 not in ("a", "b", "c", "x"):
            respuesta_12 = input(
                RED +
                "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_12 == "c":
            score += 10
            correctas += 1
            print(GREEN + "\nLa respuesta es correcta!\n" + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_12 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(RED + "\nIncorrecto" + RESET, nombre,
                  GREEN + "la respuesta es 'los pixeles'\n" + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 13:" + RESET)
        print(
            BLACK +
            "\n¿Cuál de estos elementos es responsable de la administración y coordinación de actividades y la división de recursos del ordenador?\n"
            + RESET)
        print(CYAN + "a) Placa base" + RESET)
        print(CYAN + "b) Sistema operativo" + RESET)
        print(CYAN + "c) RAM" + RESET)
        respuesta_13 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_13 not in ("a", "b", "c", "x"):
            respuesta_13 = input(
                RED +
                "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_13 == "b":
            score += 10
            correctas += 1
            print(GREEN + "\nLa respuesta es correcta!\n" + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_13 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(RED + "\nIncorrecto" + RESET, nombre,
                  GREEN + "la respuesta es el sistema operativo\n" + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 14:" + RESET)
        print(BLACK + "\n¿Desde cuándo podemos copiar y pegar?\n" + RESET)
        print(CYAN + "a) Desde 1981" + RESET)
        print(CYAN + "b) Desde 1984" + RESET)
        print(CYAN + "c) Desde 1986" + RESET)
        respuesta_14 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_14 not in ("a", "b", "c", "x"):
            respuesta_14 = input(
                RED +
                "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_14 == "a":
            score += 10
            correctas += 1
            print(
                GREEN +
                "\nMuy bien! En 1981, el ingeniero Larry Tesler desarrolló esta función que nos ahorra tantas horas de trabajo.\n"
                + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_14 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es la 'a'. Él ingeniero Larry Tesler desarrolló esta función que nos ahorra tantas horas de trabajo.\n "
                + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 15:" + RESET)
        print(
            BLACK +
            "\n¿Cuál de los siguientes comandos o atajos de teclado puede utilizarse para cambiar a mayúsculas o minúsculas?\n"
            + RESET)
        print(CYAN + "a) CONTROL+SHIFT+F3" + RESET)
        print(CYAN + "b) SHIFT + F3" + RESET)
        print(CYAN + "c) ALT + F3" + RESET)
        respuesta_15 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_15 not in ("a", "b", "c", "x"):
            respuesta_15 = input(
                RED +
                "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_15 == "b":
            score += 10
            correctas += 1
            print(GREEN + "\nLa respuesta es correcta!\n" + RESET)
            print(YELLOW + f"Tienes {score} puntos" + RESET)
        elif respuesta_15 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(RED + "\nIncorrecto" + RESET, nombre,
                  GREEN + "la respuesta es SHIFT + F3\n" + RESET)
            score -= 5
            incorrectas += 1
            print(RED + f"Tienes {score} puntos" + RESET)
        print(BLUE + "\npregunta 16:" + RESET)
        print(BLACK +
              "\n¿Cuál de estos sistemas operativos nunca vio la luz?\n" +
              RESET)
        print(CYAN + "a) Peppermint 10" + RESET)
        print(CYAN + "b) Q4OS 3" + RESET)
        print(CYAN + "c) Windows 9" + RESET)
        respuesta_16 = input(YELLOW + "\nTu respuesta: " + RESET)
        while respuesta_16 not in ("a", "b", "c", "x"):
            respuesta_16 = input(
                RED +
                "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
                RESET)
        if respuesta_16 == "c":
            score += 10
            correctas += 1
            print(GREEN +
                  "\nCorrecto! Microsoft saltó de la versión 8 a la 10!\n" +
                  RESET)
        elif respuesta_16 == "x":
            print(BLUE + "\nMensaje secreto desbloqueado:\n" + RESET)
            print(GREEN + "¡Tu puedes hacer todo lo que te propongas!" + RESET)
        else:
            print(
                RED + "\nIncorrecto" + RESET,
                nombre,
            )
            print(
                GREEN +
                "\nLa respuesta es la C.Microsoft saltó de la versión 8 a la 10!"
                + RESET)
            score -= 5
            incorrectas += 1
        print(YELLOW + "\nFELICIDADES POR COMPLETAR LA TRIVIA!!!" + RESET)
        print(f"""\n
        {BLUE}Tu puntuacion final es: {score}
        
        Respuestas correctas: {correctas}
        
        Respuestas incorrectas: {incorrectas}
        {RESET}\n""")

        while True:
            finish = input(GREEN +
                           "Deseas volver a jugar la trivia: si o no " +
                           RESET).lower()
            if finish == "si":
                break
            elif finish == "no":
                print(YELLOW +
                      "\nRegresa cuando estes listo para hacer la trivia" +
                      RESET)
                exit()
            else:
                print(RED + "Valor incorrecto, ingrese si o no: " + RESET)

    else:
        print(YELLOW + "Regresa cuando estes listo para hacer la trivia" +
              RESET)
        break
