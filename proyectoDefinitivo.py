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
    # detener cualquier música previa antes de iniciar otra
    pygame.mixer.music.stop()
    hilo = threading.Thread(target=music, args=(x,))
    hilo.start()

# --- Funciones ---
def ajustes():
    ventanaAjustes = tkinter.Toplevel()
    ventanaAjustes.title("Wispers: Los Ajustes")
    ventanaAjustes.geometry("450x300")

    # Fondo de ajustes
    fondo_ajustes = tkinter.PhotoImage(file="i/fa.png")
    canvas_ajustes = tkinter.Canvas(ventanaAjustes, width=450, height=300)
    canvas_ajustes.create_image(0, 0, image=fondo_ajustes, anchor="nw")
    canvas_ajustes.pack(fill="both", expand=True)
    canvas_ajustes.image = fondo_ajustes  # mantener referencia

    # Botones de música
    botm1 = tkinter.PhotoImage(file="i/bm1.png")
    botm2 = tkinter.PhotoImage(file="i/bm2.png")
    botm3 = tkinter.PhotoImage(file="i/bm3.png")

    boton_m1 = tkinter.Button(ventanaAjustes, image=botm1, command=lambda: iniciar_musica(1))
    boton_m1.image = botm1
    boton_m2 = tkinter.Button(ventanaAjustes, image=botm2, command=lambda: iniciar_musica(2))
    boton_m2.image = botm2
    boton_m3 = tkinter.Button(ventanaAjustes, image=botm3, command=lambda: iniciar_musica(3))
    boton_m3.image = botm3

    # Botón Stop con imagen
    imagen_stop = tkinter.PhotoImage(file="i/bms.png")
    boton_stop = tkinter.Button(ventanaAjustes, image=imagen_stop, command=lambda: iniciar_musica(0))
    boton_stop.image = imagen_stop

    # Colocar botones dentro del canvas
    canvas_ajustes.create_window(100, 40, window=boton_m1)
    canvas_ajustes.create_window(100, 80, window=boton_m2)
    canvas_ajustes.create_window(100, 120, window=boton_m3)
    canvas_ajustes.create_window(250, 40, window=boton_stop)

def juegoiniciado():
    print("Juego iniciado")

# --- Fondo principal ---
imagen_fondo1 = tkinter.PhotoImage(file="i/f1.png")
canvas_pantallainicio = tkinter.Canvas(ventanaPrincipal, width=1024, height=768, bg="white")
canvas_pantallainicio.create_image(0, 0, image=imagen_fondo1, anchor="nw")
canvas_pantallainicio.pack(fill="both", expand=True)
canvas_pantallainicio.image = imagen_fondo1  # mantener referencia

# --- Botones inicio ---
imagen_play = tkinter.PhotoImage(file="i/bs.png")
imagen_ajustes = tkinter.PhotoImage(file="i/ba.png")

boton_play = tkinter.Button(ventanaPrincipal, image=imagen_play, command=juegoiniciado)
boton_play.place(x=400, y=300)

boton_ajustes = tkinter.Button(ventanaPrincipal, image=imagen_ajustes, command=ajustes)
boton_ajustes.place(x=400, y=400)

ventanaPrincipal.mainloop()

