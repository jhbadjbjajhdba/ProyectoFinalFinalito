import tkinter
import time
import threading
import pygame
# pip install playsound

ventanaPrincipal = tkinter.Tk()   # Creación de Ventana
ventanaPrincipal.title("Wispers")   # Da nombre a la ventana
ventanaPrincipal.geometry("1024x768")   # La dimención de la ventana.

def ajustes():
    ventanaAjustes = tkinter.Toplevel
    ventanaAjustes.title("Wispers: Los Ajustes")
    musica = False


    ventanaAjustes.pack()


#Musica:
def music(x):
    pygame.mixer.init()  # iniciar el sistema de audio
    if(x==1):
        
        pygame.mixer.music.load("./i/m1.mp3")  # cargar archivo
        pygame.mixer.music.play(-1)              # reproducir

    if(x==2):

        pygame.mixer.music.load("./i/m2.mp3")  # cargar archivo
        pygame.mixer.music.play(-1)              # reproducir
    if(x==3):
        pygame.mixer.music.load("./i/m3.mp3")  # cargar archivo
        pygame.mixer.music.play(-1)              # reproducir
    if(x==0):
         pygame.mixer.music.stop() 

musica = threading.Thread(target= music,args=)

def boton_musica_1():
    


#def juegoiniciado()

imagen_fondo1 = tkinter.PhotoImage(file= "./i/f1.png")
canvas_pantallainicio = tkinter.canvas(ventanaPrincipal, width=1024, height=768, bg="white")
canvas_pantallainicio.create_image(image= imagen_fondo1)
canvas_pantallainicio.pack()

ventanaPrincipal.pack

