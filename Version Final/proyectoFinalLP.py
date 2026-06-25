import sys
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

# Si la persona que va a jugar no tiene instalada la librería Pillow (para las imágenes),
# este bloque la instala automáticamente para que el juego no tenga fallos.
try:
    from PIL import Image, ImageTk
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageTk

# Guardamos el progreso del juego en un diccionario.
# Así es más ordenado saber qué mascota ya está a salvo.
estado_juego = {
    "Lucky": {"rescatado": False},
    "Chester": {"rescatado": False},
    "Nala": {"rescatado": False}
}

# Esta función nos sirve para asegurar que el usuario solo escriba "si" o "no".
# Si pone cualquier otra cosa, le lanza un error y le recuerda las instrucciones.
def pedir_respuesta_si_no(titulo, pregunta, instrucciones):
    while True:
        # Se agrega parent=ventana para que el cuadro de texto NO se vaya para atrás
        respuesta = simpledialog.askstring(titulo, pregunta, parent=ventana)
        # Si el usuario cierra la ventana, cancelamos la acción.
        if respuesta is None:  
            return None
        
        # Limpiamos el texto: lo pasamos a minúsculas y le quitamos espacios extra.
        respuesta = respuesta.lower().strip()
        if respuesta in ["si", "no"]:
            return respuesta
        else:
            # Mostramos el error sin emojis y volvemos a cargar las instrucciones (siempre arriba).
            messagebox.showwarning("Entrada invalida", "Por favor, responde estrictamente con 'si' o 'no'.", parent=ventana)
            messagebox.showinfo(f"Recordatorio - {titulo}", instrucciones, parent=ventana)

# Vuelve a poner a todas las mascotas como no rescatadas (False) para iniciar otra partida.
def reiniciar_juego():
    for mascota in estado_juego:
        estado_juego[mascota]["rescatado"] = False
    actualizar_interfaz() 
    messagebox.showinfo("Reinicio Exitoso", "El juego se ha reiniciado, las mascotas estan escondidas de nuevo.", parent=ventana)

# Esta es la ventana final que aparece cuando ganas el juego, mostrando la imagen editada.
def mostrar_pantalla_victoria():
    ventana_victoria = tk.Toplevel(ventana)
    ventana_victoria.title("Mision Cumplida!")
    ventana_victoria.geometry("450x620")
    ventana_victoria.configure(bg="#2f3640")
    
    # Intentamos cargar la imagen "victoria.jpeg". Si no la encuentra, mostramos un texto de error.
    try:
        img_original = Image.open("victoria.jpeg")
        img_redimensionada = img_original.resize((400, 500), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_redimensionada)
        
        lbl_img = tk.Label(ventana_victoria, image=img_tk, bg="#2f3640")
        lbl_img.image = img_tk # Guardamos la imagen en memoria para que no se borre
        lbl_img.pack(pady=(15, 5))
    except Exception as e:
        tk.Label(ventana_victoria, text="[Imagen 'victoria.jpeg' no encontrada]", fg="#ff7675", bg="#2f3640").pack(pady=20)

    # Texto de felicitación y botón para cerrar (aquí sí conservamos emojis en el diseño).
    tk.Label(ventana_victoria, text=" ¡FELICIDADES! \nHas dominado la lógica básica de la programación!.", font=("Segoe UI", 11, "bold"), bg="#2f3640", fg="#fbc531").pack(pady=5)
    tk.Button(ventana_victoria, text="Genial", command=ventana_victoria.destroy, width=15, bg="#4cd137", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2").pack(pady=5)

# Revisa si las tres mascotas ya tienen el estado "True" (rescatadas). Si es así, lanza la victoria.
def verificar_victoria():
    if estado_juego["Lucky"]["rescatado"] and estado_juego["Chester"]["rescatado"] and estado_juego["Nala"]["rescatado"]:
        mostrar_pantalla_victoria()
    actualizar_interfaz()

# Cambia el color y el texto de los botones del menú cuando rescatas a una mascota.
def actualizar_interfaz():
    color_lucky = "#7f8fa6" if estado_juego["Lucky"]["rescatado"] else "#00a8ff"
    color_chester = "#7f8fa6" if estado_juego["Chester"]["rescatado"] else "#4cd137"
    color_nala = "#7f8fa6" if estado_juego["Nala"]["rescatado"] else "#e1b12c"

    btn_lucky.config(text="✔️ Lucky (RESCATADO)" if estado_juego["Lucky"]["rescatado"] else "📍 Zona 1: El Río (Lucky)", bg=color_lucky)
    btn_chester.config(text="✔️ Chester (RESCATADO)" if estado_juego["Chester"]["rescatado"] else "📍 Zona 2: Mariposario (Chester)", bg=color_chester)
    btn_nala.config(text="✔️ Nala (RESCATADO)" if estado_juego["Nala"]["rescatado"] else "📍 Zona 3: La Cabaña (Nala)", bg=color_nala)

# --------------------------------------------------------
# NIVELES DEL JUEGO (ZONAS Y COMPUERTAS)
# --------------------------------------------------------

# ZONA 1: Compuerta AND. Las dos condiciones deben ser ciertas para ganar.
def zona_rio_lucky():
    # Si ya lo rescatamos, no nos deja volver a jugar este nivel.
    if estado_juego["Lucky"]["rescatado"]:
        messagebox.showinfo("Zona 1", "Tu perrito Lucky ya esta a salvo y mueve su colita a tu lado.", parent=ventana)
        return

    intro = ("Narrador: Lucky ha quedado atrapado al otro lado del río.\n\n"
             "LECCIÓN LÓGICA: Conoce a la compuerta 'AND'\n"
             "La regla es estricta. Exige que TODAS las condiciones sean verdaderas al mismo tiempo.\n\n"
             "Para que Lucky cruce, necesitas tener comida (para atraerlo) Y una correa (para asegurarlo), si te falta alguna de las dos, no cruzará.")
    messagebox.showinfo("Zona 1: Salva a Lucky", intro, parent=ventana)
    
    # Pedimos las respuestas pasando las instrucciones por si el jugador se equivoca.
    resp_comida = pedir_respuesta_si_no("Compuerta AND", "¿Tienes comida en tu mochila? (si/no):", intro)
    if resp_comida is None: return
    
    resp_correa = pedir_respuesta_si_no("Compuerta AND", "¿Tienes una correa en tu mochila? (si/no):", intro)
    if resp_correa is None: return

    # Evaluamos con AND: si tiene comida Y tiene correa
    if resp_comida == "si" and resp_correa == "si":
        mensaje_exito = "¡VERDADERO + VERDADERO = VERDADERO!\n\n¡Excelente deducción! Al cumplir estrictamente ambas condiciones, tu perrito Lucky cruzó el río sin miedo y ya está a salvo en tus brazos. \n\n ¡Lograste cumplir con la lógica de la compuerta AND! "
        messagebox.showinfo("Exito logico!", mensaje_exito, parent=ventana)
        estado_juego["Lucky"]["rescatado"] = True
    else:
        val1 = "VERDADERO" if resp_comida == "si" else "FALSO"
        val2 = "VERDADERO" if resp_correa == "si" else "FALSO"
        mensaje_fallo = f"¡{val1} + {val2} = FALSO!\n\nLa regla falló. Necesitas cumplir AMBAS condiciones a la vez. Inténtalo de nuevo."
        messagebox.showwarning("Fallo logico", mensaje_fallo, parent=ventana)
    
    verificar_victoria()

# ZONA 2: Compuerta OR. Basta con que una condición sea cierta para ganar.
def zona_mariposario_chester():
    if estado_juego["Chester"]["rescatado"]:
        messagebox.showinfo("Zona 2", "Tu perrito Chester ya esta a salvo contigo pidiendo mimos.", parent=ventana)
        return

    intro = ("Narrador: Chester está hipnotizado persiguiendo mariposas de colores ¡necesita salir de ese lugar!.\n\n"
             "LECCIÓN LÓGICA: Compuerta 'OR'\n"
             "La regla es flexible. Funciona si AL MENOS UNA de las condiciones es verdadera o incluso si AMBAS lo son.\n\n"
             "Chester irá contigo si le ofreces su premio favorito, si haces sonar su juguete ruidoso o los dos al mismo tiempo.")
    messagebox.showinfo("Zona 2: Salva a Chester", intro, parent=ventana)
    
    resp_premio = pedir_respuesta_si_no("Compuerta OR", "¿Quieres ofrecerle su premio favorito? (si/no):", intro)
    if resp_premio is None: return
    
    resp_juguete = pedir_respuesta_si_no("Compuerta OR", "¿Quieres hacer sonar su juguete ruidoso? (si/no):", intro)
    if resp_juguete is None: return

    val_premio = "VERDADERO" if resp_premio == "si" else "FALSO"
    val_juguete = "VERDADERO" if resp_juguete == "si" else "FALSO"

    # Evaluamos los tres casos posibles del OR para narrarlo mejor
    if resp_premio == "si" and resp_juguete == "si":
        mensaje_exito = f"¡{val_premio} + {val_juguete} = VERDADERO!\n\n¡Hiciste ambas cosas! Le ofreciste su premio y sonaste su juguete. Como la regla es flexible, permite que ambas acciones sean verdaderas. ¡Chester corrió rapidísimo hacia ti! \n\n ¡Lograste cumplir con la lógica de la compuerta OR!"
        messagebox.showinfo("Exito logico!", mensaje_exito, parent=ventana)
        estado_juego["Chester"]["rescatado"] = True
    elif resp_premio == "si" or resp_juguete == "si":
        mensaje_exito = f"¡{val_premio} + {val_juguete} = VERDADERO!\n\n¡Muy bien! Como la regla es flexible, bastó con que una sola acción funcionara. Tu perrito Chester dejó de perseguir mariposas y corrió feliz hacia ti.\n\n ¡Lograste cumplir con la lógica de la compuerta OR!"
        messagebox.showinfo("Exito logico!", mensaje_exito, parent=ventana)
        estado_juego["Chester"]["rescatado"] = True
    else:
        mensaje_fallo = f"¡{val_premio} + {val_juguete} = FALSO!\n\nNo hiciste nada para llamar su atención, sigue persiguiendo a las mariposas."
        messagebox.showwarning("Fallo logico", mensaje_fallo, parent=ventana)
    
    verificar_victoria()

# ZONA 3: Compuerta XOR y Bucle FOR. Solo una opción debe ser cierta y hay 3 intentos.
def zona_cabana_nala():
    if estado_juego["Nala"]["rescatado"]:
        messagebox.showinfo("Zona 3", "Tu gatita Nala ya esta a salvo y ronroneando.", parent=ventana)
        return

    intro = ("Narrador: Nala está atrapada en una cabaña ¡necitas abrir la puerta!.\n\n"
             "LECCIÓN LÓGICA: Compuerta 'XOR' \n"
             "La regla exige exclusividad estricta. El resultado solo es VERDADERO si las entradas son diferentes.\n\n"
             "Para abrir la puerta, debes presionar EXACTAMENTE UN botón (uno 'si' y el otro 'no').\n"
             "• Si presionas ambos botones ('si' y 'si'), el sistema falla.\n"
             "• Si no presionas ninguno de los botones ('no' y 'no'), el sistema también falla.\n\n"
             "¡Tienes solo 3 intentos!")
    messagebox.showinfo("Zona 3: Salva a Nala", intro, parent=ventana)

    # Usamos un bucle for para darle 3 intentos al jugador
    for intento in range(1, 4):
        resp_rojo = pedir_respuesta_si_no(f"Intento {intento}/3", "¿Presionas el botón ROJO? (si/no):", intro)
        if resp_rojo is None: return
        
        resp_azul = pedir_respuesta_si_no(f"Intento {intento}/3", "¿Presionas el botón AZUL? (si/no):", intro)
        if resp_azul is None: return
        
        # Convertimos el texto a booleanos puros de Python
        boton_rojo = (resp_rojo == "si")
        boton_azul = (resp_azul == "si")

        val_rojo = "VERDADERO" if boton_rojo else "FALSO"
        val_azul = "VERDADERO" if boton_azul else "FALSO"

        # El símbolo ^ evalúa la lógica XOR en Python
        if boton_rojo ^ boton_azul:
            mensaje_exito = f"¡{val_rojo} + {val_azul} = VERDADERO!\n\n¡Lógica perfecta! Al presionar solo un botón, la puerta se abrió. Tu gatita Nala saltó libre de la cabaña y está a salvo. \n\n ¡Lograste cumplir con la lógica de la compuerta XOR!"
            messagebox.showinfo("Exito logico!", mensaje_exito, parent=ventana)
            estado_juego["Nala"]["rescatado"] = True
            break  # Detenemos el bucle porque ya ganó
        else:
            # Si falló, revisamos si le quedan intentos
            if intento < 3:
                mensaje_fallo = f"¡{val_rojo} + {val_azul} = FALSO!\n\n¡Error de exclusividad! Recuerda: las entradas deben ser diferentes. La puerta sigue cerrada."
                messagebox.showwarning("Fallo logico", mensaje_fallo, parent=ventana)
            else:
                messagebox.showerror("Bloqueo del Sistema", "Has fallado 3 veces. El sistema de la cabaña se ha bloqueado temporalmente, vuelvelo a intentar.", parent=ventana)
    
    verificar_victoria()

# --------------------------------------------------------
# DISEÑO DE LA INTERFAZ GRÁFICA
# --------------------------------------------------------
ventana = tk.Tk()
ventana.title("MindoLogic - Aprendiendo Lógica de Programación")
ventana.geometry("500x560")
ventana.configure(bg="#2f3640") 

# Estilos de texto
fuente_titulo = ("Segoe UI", 16, "bold")
fuente_sub = ("Segoe UI", 10)
fuente_nota = ("Segoe UI", 9, "italic")
fuente_btn = ("Segoe UI", 12, "bold")

# Títulos principales y notas (Aquí sí van los emojis decorativos)
tk.Label(ventana, text="🧠 MindoLogic: Misión Rescate en Mindo", font=fuente_titulo, bg="#2f3640", fg="#fbc531").pack(pady=(25, 5))
tk.Label(ventana, text="Aprende cómo piensan las computadoras rescatando mascotas y utilizando las compuertas lógicas (AND, OR y XOR).", font=fuente_sub, bg="#2f3640", fg="#dcdde1").pack(pady=(0, 5))
tk.Label(ventana, text="⚠️ Nota: El sistema solo aceptará las respuestas solicitadas (ej. 'si' o 'no').", font=fuente_nota, bg="#2f3640", fg="#ff7675").pack(pady=(0, 20))

# Agrupamos los botones de los niveles en este contenedor
frame_zonas = tk.Frame(ventana, bg="#2f3640")
frame_zonas.pack(pady=10)

# Creamos los botones y los enlazamos a sus respectivas funciones
btn_lucky = tk.Button(frame_zonas, text="📍 Zona 1: El Río (Lucky)", command=zona_rio_lucky, width=30, bg="#00a8ff", fg="white", font=fuente_btn, relief="flat", cursor="hand2", pady=8)
btn_lucky.pack(pady=10)

btn_chester = tk.Button(frame_zonas, text="📍 Zona 2: Mariposario (Chester)", command=zona_mariposario_chester, width=30, bg="#4cd137", fg="white", font=fuente_btn, relief="flat", cursor="hand2", pady=8)
btn_chester.pack(pady=10)

btn_nala = tk.Button(frame_zonas, text="📍 Zona 3: La Cabaña (Nala)", command=zona_cabana_nala, width=30, bg="#e1b12c", fg="white", font=fuente_btn, relief="flat", cursor="hand2", pady=8)
btn_nala.pack(pady=10)

# Una línea gris decorativa para separar los niveles del botón de reinicio
tk.Frame(ventana, height=1, bg="#7f8fa6", width=400).pack(pady=15)

# Botón para reiniciar
btn_reinicio = tk.Button(ventana, text="🔄 Reiniciar Nivel", command=reiniciar_juego, width=20, bg="#e84118", fg="white", font=("Segoe UI", 11, "bold"), relief="flat", cursor="hand2", pady=10)
btn_reinicio.pack()

# Mantiene la ventana abierta esperando a que el jugador haga clic
ventana.mainloop()