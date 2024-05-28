#Interfaz Kiosco Multimedia
#Autores: Ramirez Andres Daniela, Gonzalez Aguilar Julio Cesar
#Fecha: 28 de Mayo de 2024
#Descripcion: Kiosko Multimedia que accede a servicios en linea y reproduce contenido digital de una USB
#Licencia: MIT

import customtkinter as ctk
import tkinter as tk
import subprocess
import pygame
import threading
from montar_usb import *

def abrir_netflix():
	subprocess.Popen(["/bin/chromium-browser", "--app=https://www.netflix.com", "--start-fullscreen", "--window-size=1920,1080"])

def abrir_prime_video():
	subprocess.Popen(["/bin/chromium-browser", "--app=https://www.primevideo.com", "--start-fullscreen","--window-size=1920,1080"])

def abrir_vix():
	subprocess.Popen(["/bin/chromium-browser", "--app=https://www.vix.com/es", "--start-fullscreen", "--window-size=1920,1080" ])

def abrir_spotify():
	subporcess.Popen(["/bin/chromium-browser", "--app=https://www.spotify.com", "--start-fullscreen", "window-size=1920,1080"])

def abrir_deezer():
	subprocess.Popen(["/bin/chromium-browser", "--app=https://www.deezer.com", "--start-fullscreen", "window-size=1920,1080"])

def abrir_amazon_music():
	subprocess.Popen(["/bin/chromium-browser", "--app=https://www.music.amazon.com", "--start-fullscreen", "window-size=1920,1080"])

def salir_interfaz():
	ventana.destroy()

def usb_imagen():
	medios=[]
	#mp=main_vlc()
	if any(file.endswith((".jpg", ".png")) for file in os.listdir(mp)):
		medios.append("imagenes")
	if any(file.endswith((".mp3", ".wav")) for file in os.listdir(mp)):
		medios.append("audio")
	if any(file.endswith((".mp4", ".avi")) for file in os.listdir(mp)):
		medios.append("video")

	if len(medios)!=0:
		fotos=[os.path.join(mp,f) for f in os.listdir(mp) if f.endswith((".jpg", ".png"))]
		reproducir_presentacion(fotos)
def usb_audio():
	medios=[]
	#mp=main_vlc()
	if any(file.endswith((".jpg", ".png")) for file in os.listdir(mp)):
		medios.append("imagenes")
	if any(file.endswith((".mp3", ".wav")) for file in os.listdir(mp)):
		medios.append("audio")
	if any(file.endswith((".mp4", ".avi")) for file in os.listdir(mp)):
		medios.append("video")

	if len(medios)!=0:
		music=[os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".mp3", ".wav"))]
		if music:
			reproducir_musica(music)

def usb_video():
	medios=[]
	#mp=main_vlc()
	if any(file.endswith((".jpg", ".png")) for file in os.listdir(mp)):
		medios.append("imagenes")
	if any(file.endswith((".mp3", ".wav")) for file in os.listdir(mp)):
		medios.append("audio")
	if any(file.endswith((".mp4", ".avi")) for file in os.listdir(mp)):
		medios.append("video")

	if len(medios)!=0:
		videos=[os.path.join(mp,f) for f in os.listdir(mp) if f.endswith((".mp4", ".avi"))]
		reproducir_video(videos)
global mp
mp=main_vlc()		
ventana = tk.Tk()
ventana.attributes('-fullscreen',True)
ventana.title("SmartTv")

icono_netflix = tk.PhotoImage(file="/home/jules/proyecto/images/netflix_icon.png")
icon_prime_video = tk.PhotoImage(file="/home/jules/proyecto/images/prime_video_icon.png")
icon_spotify = tk.PhotoImage(file="/home/jules/proyecto/images/spotify_icon.png")
icon_amazon_music = tk.PhotoImage(file="/home/jules/proyecto/images/amazon_music_icon.png")
icon_vix = tk.PhotoImage(file="/home/jules/proyecto/images/vix_icon.png")
icon_deezer = tk.PhotoImage(file="/home/jules/proyecto/images/deezer_icon.png")
icon_usb = tk.PhotoImage(file="/home/jules/proyecto/images/usb_icon.png")
icon_imagen = tk.PhotoImage(file="/home/jules/proyecto/images/imagen_icon.png")
icon_audio = tk.PhotoImage(file="/home/jules/proyecto/images/audio_icon.png")
icon_video = tk.PhotoImage(file="/home/jules/proyecto/images/video_icon.png")

##frames
frame_left = tk.Frame(ventana, bg="black", width=400)
frame_top = tk.Frame(ventana)
frame_bottom = tk.Frame(ventana)
frame_exit = tk.Frame(ventana)

#etiquetas frame izquierdo
label_bienvenido = tk.Label(frame_left, text="Bienvenido  a JulesTV", bg="black", fg="white", font=("Helvetica", 20, "bold"))
label_inicio = tk.Label(frame_left, text="Inicio", bg="black", fg="white", font=("Helvetica", 14))



label_bienvenido.pack(pady=20)
label_inicio.pack(pady=10)



boton_netflix = tk.Button(frame_bottom, image=icono_netflix, width = 300, height = 300)
boton_netflix.config(command=abrir_netflix)

boton_prime_video = tk.Button(frame_top, image=icon_prime_video, width = 300, height = 300)
boton_prime_video.config(command=abrir_prime_video)

boton_spotify = tk.Button(frame_top, image=icon_spotify, width = 300, height = 300)
boton_spotify.config(command=abrir_spotify)

boton_amazon_music = tk.Button(frame_bottom, image=icon_amazon_music, width = 300, height = 300)
boton_amazon_music.config(command=abrir_amazon_music)

boton_vix = tk.Button(frame_bottom, image=icon_vix, width = 300, height = 300)
boton_vix.config(command=abrir_vix)

boton_deezer = tk.Button(frame_bottom, image=icon_deezer, width = 300, height = 300)
boton_deezer.config(command=abrir_deezer)

#boton_usb = tk.Button(frame_top, image=icon_usb, width = 300, height = 300)
#boton_usb.config(command=usb)

boton_imagen = tk.Button(frame_top, text="imagenes", width =10 , height = 10)
boton_imagen.config(command=usb_imagen)

boton_audio = tk.Button(frame_top, text="audio", width = 10, height = 10)
boton_audio.config(command=usb_audio)

boton_video = tk.Button(frame_top, text="video", width = 10, height = 10)
boton_video.config(command=usb_video)



boton_salir = tk.Button(frame_exit, text="salir", command=salir_interfaz, width = 20, height = 20)


#boton_usb.pack(side="left", padx=50, pady=50)
boton_imagen.pack(side="left", padx=10, pady=10)
boton_audio.pack(side="left", padx=10, pady=10)
boton_video.pack(side="left", padx=10, pady=10)



boton_netflix.pack(side="left", padx=50, pady=50)
boton_prime_video.pack(side="left", padx=50, pady=50)
boton_spotify.pack(side="left", padx=50, pady=50)
boton_amazon_music.pack(side="left", padx=50, pady=50)
boton_vix.pack(side="left", padx=50, pady=50)
boton_deezer.pack(side="left", padx=50, pady=50)
boton_salir.pack(side="right", padx=20, pady=20)

frame_left.pack(side="left", fill="y")
frame_top.pack(pady=50)
frame_bottom.pack(pady=50)
frame_exit.pack(side="bottom", anchor="e", pady=20, padx=20)

#inicializar pygfame
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()



#lista de botones
botones = [boton_netflix, boton_prime_video, boton_spotify, boton_amazon_music, boton_vix, boton_deezer, boton_imagen, boton_audio, boton_video, boton_salir]
boton_index = 0
botones[boton_index].focus_set()

#eventos del mando
def manejar_joystick():
	global boton_index
	while True:
		for event in pygame.event.get():
			if event.type == pygame.JOYAXISMOTION:
				if joystick.get_axis(1) > 0.5:
					boton_index = (boton_index + 1) % len(botones)
					botones[boton_index].focus_set()
					pygame.time.wait(200)
				elif joystick.get_axis(1) < -0.5:
					boton_index = (boton_index -1) % len(botones)
					botones[boton_index].focus_set()
					pygame.time.wait(200)
			elif event.type == pygame.JOYBUTTONDOWN:
				if joystick.get_button(0):
					botones[boton_index].invoke()


#manejador de eventos en diferente hilo
thread = threading.Thread(target=manejar_joystick)
thread.deamon = True
thread.start()

ventana.mainloop()
