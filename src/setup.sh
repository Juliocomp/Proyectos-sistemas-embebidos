#Interfaz Kiosco Multimedia
#Autores: Ramirez Andres Daniela, Gonzalez Aguilar Julio Cesar
#Fecha: 28 de Mayo de 2024
#Descripcion: setup para instalacion
#Licencia: MIT

#!/bin/bash

# Instalar pip para Python 3
sudo apt-get install python3-pip

# Instalar librerías pyudev y python-vlc
pip3 install pyudev python-vlc

# Instalar VLC y udisks2
sudo apt-get install vlc udisks2

# Actualizar el sistema
sudo apt-get update
sudo apt-get upgrade

# Instalar o actualizar Widevine
sudo apt install libwidevinecdm0 -y

# Instalar xinit y Chromium Browser
sudo apt-get install xinit chromium-browser

# Instalar dependencias Bluetooth
sudo apt install bluetooth bluez blueman

# Habilitar y iniciar el servicio Bluetooth
sudo systemctl enable bluetooth
sudo systemctl start bluetooth

# Instalar pygame para la detección del joystick
pip install pygame

# Instalar Tkinter para la interfaz gráfica
sudo apt-get install python3-tk

# Instalar el servidor X
sudo apt-get install xserver-xorg
