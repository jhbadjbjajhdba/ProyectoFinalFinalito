import tkinter
import time
import threading
import pygame
# pip install playsound

# --- Ventana principal ---
ventanaPrincipal = tkinter.Tk()
ventanaPrincipal.title("Wispers")
ventanaPrincipal.geometry("1024x768")

# Inicializar pygame mixer una sola vez
pygame.mixer.init()

# --- Música ---
def music(x):
    if x == 1:
        pygame.mixer.music.load("./i/m1.mp3")
        pygame.mixer.music.play(-1)
    elif x == 2:
        pygame.mixer.music.load("./i/m2.mp3")
        pygame.mixer.music.play(-1)
    elif x == 3:
        pygame.mixer.music.load("./i/m3.mp3")
        pygame.mixer.music.play(-1)
    elif x == 0:
        pygame.mixer.music.stop()

def iniciar_musica(x):
    pygame.mixer.music.stop()
    hilo = threading.Thread(target=music, args=(x,))
    hilo.start()

# --- Contenedor de pantallas ---
contenedor = tkinter.Frame(ventanaPrincipal)
contenedor.pack(fill="both", expand=True)

pantalla_inicio = tkinter.Frame(contenedor)
pantalla_nombre = tkinter.Frame(contenedor)
pantalla_mapa = tkinter.Frame(contenedor)
pantalla_dialogo = tkinter.Frame(contenedor)
pantalla_seleccion = tkinter.Frame(contenedor)

for frame in (pantalla_inicio, pantalla_nombre, pantalla_mapa, pantalla_dialogo, pantalla_seleccion):
    frame.grid(row=0, column=0, sticky="nsew")

# --- Ajustes ---
def ajustes():
    ventanaAjustes = tkinter.Toplevel()
    ventanaAjustes.title("Wispers: Los Ajustes")
    ventanaAjustes.geometry("450x300")

    fondo_ajustes = tkinter.PhotoImage(file="i/fa.png")
    canvas_ajustes = tkinter.Canvas(ventanaAjustes, width=450, height=300)
    canvas_ajustes.create_image(0, 0, image=fondo_ajustes, anchor="nw")
    canvas_ajustes.pack(fill="both", expand=True)
    canvas_ajustes.image = fondo_ajustes

    botm1 = tkinter.PhotoImage(file="i/bm1.png")
    botm2 = tkinter.PhotoImage(file="i/bm2.png")
    botm3 = tkinter.PhotoImage(file="i/bm3.png")

    boton_m1 = tkinter.Button(ventanaAjustes, image=botm1, command=lambda: iniciar_musica(1))
    boton_m1.image = botm1
    boton_m2 = tkinter.Button(ventanaAjustes, image=botm2, command=lambda: iniciar_musica(2))
    boton_m2.image = botm2
    boton_m3 = tkinter.Button(ventanaAjustes, image=botm3, command=lambda: iniciar_musica(3))
    boton_m3.image = botm3

    imagen_stop = tkinter.PhotoImage(file="i/bms.png")
    boton_stop = tkinter.Button(ventanaAjustes, image=imagen_stop, command=lambda: iniciar_musica(0))
    boton_stop.image = imagen_stop

    canvas_ajustes.create_window(160, 100, window=boton_m1)
    canvas_ajustes.create_window(160, 135, window=boton_m2)
    canvas_ajustes.create_window(160, 170, window=boton_m3)
    canvas_ajustes.create_window(280, 135, window=boton_stop)

# --- Pantalla inicio ---
imagen_fondo1 = tkinter.PhotoImage(file="i/f1.png")
canvas_inicio = tkinter.Canvas(pantalla_inicio, width=1024, height=768, bg="white")
canvas_inicio.create_image(0, 0, image=imagen_fondo1, anchor="nw")
canvas_inicio.pack(fill="both", expand=True)
canvas_inicio.image = imagen_fondo1

imagen_play = tkinter.PhotoImage(file="i/bs.png")
imagen_ajustes = tkinter.PhotoImage(file="i/ba.png")

boton_play = tkinter.Button(pantalla_inicio, image=imagen_play, command=lambda: pantalla_nombre.tkraise())
boton_play.place(x=400, y=300)
boton_play.image = imagen_play

boton_ajustes = tkinter.Button(pantalla_inicio, image=imagen_ajustes, command=ajustes)
boton_ajustes.place(x=400, y=400)
boton_ajustes.image = imagen_ajustes

# --- Pantalla nombre ---
imagen_nombre_fondo = tkinter.PhotoImage(file="i/fin.png")
canvas_nombre = tkinter.Canvas(pantalla_nombre, width=1024, height=768)
canvas_nombre.create_image(0, 0, image=imagen_nombre_fondo, anchor="nw")
canvas_nombre.pack(fill="both", expand=True)
canvas_nombre.image = imagen_nombre_fondo

entrada_nombre = tkinter.Entry(pantalla_nombre, font=("Arial", 20))
canvas_nombre.create_window(512, 384, window=entrada_nombre)

mensaje_error = tkinter.Label(pantalla_nombre, text="", fg="red", bg="lightblue", font=("Arial", 14))
canvas_nombre.create_window(512, 430, window=mensaje_error)

def validar_nombre():
    global nombre
    nombre = entrada_nombre.get()
    if len(nombre) < 3 or len(nombre) > 20 or nombre[0].isdigit():
        mensaje_error.config(text="Nombre inválido: 3-20 caracteres y no empezar con número")
    else:
        pantalla_mapa.tkraise()

btn_continuar = tkinter.Button(pantalla_nombre, text="Continuar", command=validar_nombre)
canvas_nombre.create_window(512, 480, window=btn_continuar)

# --- Pantalla mapa ---
imagen_mapa_fondo = tkinter.PhotoImage(file="i/m1.png")
canvas_mapa = tkinter.Canvas(pantalla_mapa, width=1024, height=768)
canvas_mapa.create_image(0, 0, image=imagen_mapa_fondo, anchor="nw")
canvas_mapa.pack(fill="both", expand=True)
canvas_mapa.image = imagen_mapa_fondo

imagen_boton_mapa = tkinter.PhotoImage(file="i/bm.png")
btn_pueblo = tkinter.Button(pantalla_mapa, image=imagen_boton_mapa, command=lambda: iniciar_dialogo())
btn_pueblo.image = imagen_boton_mapa
canvas_mapa.create_window(120, 290, window=btn_pueblo)

# --- Pantalla diálogo ---
canvas_dialogo = tkinter.Canvas(pantalla_dialogo, width=1024, height=768)
canvas_dialogo.pack(fill="both", expand=True)

imagenes_dialogo = [
    tkinter.PhotoImage(file="i/danny/d0.png"),  # burbuja vacía
    tkinter.PhotoImage(file="i/danny/d1.png"),
    tkinter.PhotoImage(file="i/danny/d2.png"),
    tkinter.PhotoImage(file="i/danny/d3.png"),
    tkinter.PhotoImage(file="i/danny/d4.png"),
    tkinter.PhotoImage(file="i/danny/d5.png"),
    tkinter.PhotoImage(file="i/danny/d6.png"),
    tkinter.PhotoImage(file="i/danny/d7.png"),
    tkinter.PhotoImage(file="i/danny/d8.png"),
    tkinter.PhotoImage(file="i/danny/d9.png"),
    tkinter.PhotoImage(file="i/danny/d10.png"),
    tkinter.PhotoImage(file="i/danny/d11.png"),
    tkinter.PhotoImage(file="i/danny/d12.png")  # "Escoge sabiamente"
]

id = 0
imagen_actual = canvas_dialogo.create_image(0, 0, image=imagenes_dialogo[id], anchor="nw")

label_nombre_dialogo = tkinter.Label(
    pantalla_dialogo,
    text="", 
    font=("Pixelify Sans", 20), 
    bg="white", 
    fg="black"
)
canvas_dialogo.create_window(512, 600, window=label_nombre_dialogo)

def iniciar_dialogo():
    global id
    id = 0
    pantalla_dialogo.tkraise()
    canvas_dialogo.itemconfig(imagen_actual, image=imagenes_dialogo[id])
    label_nombre_dialogo.config(text=f"¡{nombre}!")

def avanzar_dialogo():
    global id
    id += 1
    if id < len(imagenes_dialogo):
        canvas_dialogo.itemconfig(imagen_actual, image=imagenes_dialogo[id])
        if id > 0:
            label_nombre_dialogo.config(text="")
        if id == 12:
            pantalla_seleccion.tkraise()

btn_avanzar = tkinter.Button(pantalla_dialogo, text="Continuar", command=avanzar_dialogo)
btn_avanzar.place(x=700, y=10)


# --- Pantalla selección ---
canvas_seleccion = tkinter.Canvas(pantalla_seleccion, width=1024, height=768)
canvas_seleccion.pack(fill="both", expand=True)

fondo_seleccion = tkinter.PhotoImage(file="i/f3.png")
canvas_seleccion.create_image(0, 0, image=fondo_seleccion, anchor="nw")
canvas_seleccion.image = fondo_seleccion

wispers= ["Armadillo", "Raton", "Gato", "Zorro", "Dragon", "Caballo", "Rana", "Pinguino", "Pato", "Conejo", "Polilla", "Ardilla", "Huron", "serpiente", "Tortuga"]
tarjetaWispers = [
    armadillo= tkinter.PhotoImage(file="i\TPST1.png"),
    raton= tkinter.PhotoImage(file="i\TPST2.png"),
    gato= tkinter.PhotoImage(file="i\TPST3.png"),
    zorro= tkinter.PhotoImage(file="i\TPI1.png"),
    dragon= tkinter.PhotoImage(file="i\TPI2.png"),
    caballo= tkinter.PhotoImage(file="i\TPI3.png"),
    rana= tkinter.PhotoImage(file="i\TPN1.png"),
    pinguino= tkinter.PhotoImage(file="i\TPN2.png"),
    pato= tkinter.PhotoImage(file="i\TPN3.png"),
    conejo= tkinter.PhotoImage(file="i\TPE1.png"),
    polilla= tkinter.PhotoImage(file="i\TPE2.png"),
    ardilla= tkinter.PhotoImage(file="i\TPE3.png"),
    huron= tkinter.PhotoImage(file="i\TPSY1.png"),
    serpiente= tkinter.PhotoImage(file="i\TPSY2.png"),
    tortuga= tkinter.PhotoImage(file="i\TPSY3.png")
]
# Aquí irán los 15 botones de wispers en cuadrícula

# Mostrar inicio al arrancar
pantalla_inicio.tkraise()

ventanaPrincipal.mainloop()
