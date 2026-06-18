# ------------------------------------------------------------------------------
# PROYECTO: RESCATE EN MINDO
# OBJETIVO: Rescatar a Lucky, Chester y Nala usando lógica booleana.
# ------------------------------------------------------------------------------

print("       ¡BIENVENIDO A RESCATE EN MINDO!     ")

# 1. INICIALIZACIÓN (Estado inicial: Ninguno rescatado)
lucky_rescatado = False
chester_rescatado = False
nala_rescatada = False

# 2. BUCLE PRINCIPAL (Estructura While)
# Se repite MIENTRAS falte al menos una mascota por rescatar
while not lucky_rescatado or not chester_rescatado or not nala_rescatada:
    
    # Muestra opciones disponibles
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. El Río (Lucky)")
    print("2. El Mariposario (Chester)")
    print("3. La Cabaña (Nala)")
    
    # 3. VALIDACIÓN DE ENTRADA
    # El usuario debe ingresar estrictamente 1, 2 o 3
    opcion = ""
    while opcion not in ["1", "2", "3"]:
        opcion = input("Elige una opción para dirigirte (1-3): ").strip()
        if opcion not in ["1", "2", "3"]:
            print("Opción inválida. Ingresa 1, 2 o 3.")

    # ZONA 1: EL RÍO (Compuerta AND)
    if opcion == "1":
        if lucky_rescatado:
            print("\nLucky ya ha sido rescatado, escoge otro lugar.")
        else:
            print("\nZONA 1: EL RÍO")
            print("Narrador: Estás en el río, Lucky tiene hambre y necesita una correa.")
            
            # Validación de respuestas (solo acepta "si" o "no")
            resp_comida = ""
            while resp_comida not in ["si", "no"]:
                resp_comida = input("¿Tienes comida? (si/no): ").lower().strip()
                if resp_comida not in ["si", "no"]:
                    print("Entrada inválida. Responde 'si' o 'no'.")
            
            resp_correa = ""
            while resp_correa not in ["si", "no"]:
                resp_correa = input("¿Tienes correa? (si/no): ").lower().strip()
                if resp_correa not in ["si", "no"]:
                    print("Entrada inválida. Responde 'si' o 'no'.")

            # LÓGICA AND: Exige que AMBAS condiciones sean verdaderas
            if resp_comida == "si" and resp_correa == "si":
                print("¡Correcto! Has rescatado a Lucky.")
                lucky_rescatado = True
            else:
                print("No funcionó. Lucky no confía en tí aún. Regresas al menú.")

    # ZONA 2: EL MARIPOSARIO (Compuerta OR)
    elif opcion == "2":
        if chester_rescatado:
            print("\nChester ya ha sido rescatado.")
        else:
            print("\nZONA 2: EL MARIPOSARIO")
            print("Narrador: Estás en el mariposario. Chester solo saldrá si está lloviendo o es de noche (o las dos juntas).")
            
            # Validación de respuestas (solo acepta "si" o "no")
            resp_clima = ""
            while resp_clima not in ["si", "no"]:
                resp_clima = input("¿Está lloviendo? (si/no): ").lower().strip()
                if resp_clima not in ["si", "no"]:
                    print("Entrada inválida. Responde 'si' o 'no'.")
            
            resp_noche = ""
            while resp_noche not in ["si", "no"]:
                resp_noche = input("¿Es de noche? (si/no): ").lower().strip()
                if resp_noche not in ["si", "no"]:
                    print("Entrada inválida. Responde 'si' o 'no'.")

            # LÓGICA OR: Basta con que UNA condición sea verdadera
            if resp_clima == "si" or resp_noche == "si":
                print("¡Correcto! Has rescatado a Chester.")
                chester_rescatado = True
            else:
                print("No funcionó. Chester sigue escondido. Regresas al menú.")

    # ZONA 3: LA CABAÑA (Bucle FOR y Compuerta XOR)
    elif opcion == "3":
        if nala_rescatada:
            print("\nNala ya ha sido rescatada.")
        else:
            print("\nZONA 3: LA CABAÑA")
            print("Narrador: Estás frente a la cabaña, la puerta tiene 2 botones: rojo y azul.")
            
            # 4. BUCLE FOR (Estructura determinada)
            # Otorga exactamente 3 intentos numerados de forma secuencial (1, 2, 3)
            for intento in range(1, 4):
                print(f"\n--- Intento {intento} ---")
                
                # Validación de respuestas de los botones
                resp_rojo = ""
                while resp_rojo not in ["si", "no"]:
                    resp_rojo = input("¿Presionaste el botón rojo? (si/no): ").lower().strip()
                    if resp_rojo not in ["si", "no"]:
                        print("Entrada inválida. Responde 'si' o 'no'.")

                resp_azul = ""
                while resp_azul not in ["si", "no"]:
                    resp_azul = input("¿Presionaste el botón azul? (si/no): ").lower().strip()
                    if resp_azul not in ["si", "no"]:
                        print("Entrada inválida. Responde 'si' o 'no'.")

                # Convertir texto a booleano (True/False) para evaluar el XOR
                boton_rojo = (resp_rojo == "si")
                boton_azul = (resp_azul == "si")

                # LÓGICA XOR (^): Exige que EXCLUSIVAMENTE un botón esté activo
                if boton_rojo ^ boton_azul:
                    print("¡Correcto! Has rescatado a Nala.")
                    nala_rescatada = True
                    break  # Rompe el bucle For porque el jugador ya acertó
                else:
                    print("No funcionó. Esa combinación no abre la puerta.")
                    
                    # Verifica si es el último intento para mostrar el bloqueo
                    if intento == 3:
                        print("Se agotaron los 3 intentos. La puerta se bloquea. Regresas al menú.")

# 5. FIN DEL JUEGO
# Se ejecuta solo cuando el bucle While termina (todas las banderas son True)
print("¡FELICIDADES! Has rescatado a las tres mascotas.")
print("¡Misión cumplida!")