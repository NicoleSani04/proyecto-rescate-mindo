# 🧠 MindoLogic: Misión Rescate en Mindo

¡Bienvenido a MindoLogic! Un proyecto educativo desarrollado en Python con interfaz gráfica (`tkinter`) diseñado para enseñar la lógica básica de programación y el funcionamiento de las compuertas lógicas (AND, OR, XOR) a través de una divertida aventura de rescate de mascotas.

## 🎮 Sobre el Proyecto

En este juego, el jugador asume el rol de un rescatista en Mindo. Para lograr salvar a las tres mascotas perdidas (Lucky, Chester y Nala), el usuario deberá responder a distintas situaciones utilizando estrictamente la lógica de las compuertas computacionales:

* 🐶 **Zona 1 (El Río) - Compuerta AND:** Para rescatar a Lucky, se deben cumplir **todas** las condiciones (Verdadero + Verdadero).
* 🐕 **Zona 2 (Mariposario) - Compuerta OR:** Chester se salvará si se cumple **al menos una** o ambas condiciones (Verdadero + Falso / Verdadero + Verdadero).
* 🐈 **Zona 3 (La Cabaña) - Compuerta XOR y Bucle FOR:** La gata Nala requiere exclusividad estricta (Verdadero + Falso). Además, se implementa un bucle `for` que limita al jugador a un máximo de 3 intentos.

## 📂 Estructura del Repositorio

El proyecto está organizado en dos etapas principales que documentan el progreso del desarrollo:

* 📁 **`Version 1/`**: Contiene la iteración inicial del proyecto.
    * 📄 `main.py`: Código base del juego.
    * 📊 `DiagramasDeFlujo.png`: Diagramas que explican la lógica de programación empleada.
    * 📑 `APA2-NicoleSani.pdf`: Documentación del proyecto.
    * 🎬 `video1119569270.mp4`: Demostración en video del funcionamiento.
* 📁 **`Version Final/`**: Contiene la versión pulida del juego.
    * 📁 `Archivos/`: Recursos complementarios.
    * 📁 `Programa/`: Código final donde se ha solucionado el error de carga de la imagen de victoria, garantizando una ejecución estable.

## 🛠️ Requisitos y Ejecución

El juego está diseñado para ser muy amigable con el usuario final, incluso si no tiene experiencia instalando dependencias.

1.  **Python:** Asegúrate de tener Python 3.x instalado en tu sistema.
2.  **Librería Pillow:** El juego utiliza la librería `Pillow` para procesar la imagen final. ¡No te preocupes por instalarla a mano! El propio código tiene un bloque `try-except` que **instalará la librería automáticamente** si detecta que no la tienes.
3.  **Imagen de Victoria:** Es necesario que el archivo `victoria.jpeg` se encuentre en la misma carpeta que tu archivo `.py` principal para que la pantalla final de la misión cumplida se muestre correctamente.

**Para iniciar el juego:**
Abre tu terminal, navega hasta la carpeta del programa y ejecuta:
```bash
python main.py

Autores
Nicole Sani - Desarrollo, Lógica y Diseño - NicoleSani04 / Coni0406
