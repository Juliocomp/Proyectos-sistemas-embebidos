#Interfaz Kiosco Multimedia
#Autores: Ramirez Andres Daniela, Gonzalez Aguilar Julio Cesar
#Fecha: 28 de Mayo de 2024
#Descripcion: Montar una USB en RaspbianOS
#Licencia: MIT
import os
import pyudev
import subprocess as sp
import vlc
import time 


def print_dev_stats(path):
        photos = []
        music = []
        for file in os.listdir(path):
                if file.endswith((".jpg", ".png")):
                        photos.append(file)
                elif file.endswith((".mp3", ".wav")):
                        music.append(file)
        print("{} has {} photos and {} music file. ".format(path, len(photos), len(music)))

def auto_mount(path):
        print("Mounting device", path)
        args = ["udisksctl", "mount", "-b", path]
        sp.run(args)

def get_mount_point(path):
        args = ["findmnt", "-unl", "-S", path]
        cp = sp.run(args, capture_output=True, text=True)
        out = cp.stdout.split(" ")[0]
        return out

def reproducir_presentacion(fotos):
        for image in fotos:
                player=vlc.MediaPlayer(image)
                player.play()
                time.sleep(5)
                player.stop()

       
def reproducir_musica(music_path):
        #player = vlc.MediaPlayer(music_path)
        #player.play()
        #while True:
        #        pass
        for song in music_path:
                player=vlc.MediaPlayer(song)
                player.play()
                time.sleep(15)
                player.stop()

def reproducir_video(video):
	
	for x in video:	
        	media = vlc.MediaPlayer(x)
        	#media_player.set_media(media)
        	media.play()
        	time.sleep(10)
        	media.stop()





def main_vlc():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem="block", device_type="partition")
    


    mp=''
    while mp=='':
            action, device = monitor.receive_device()
            if action != "add":
                    continue
            print("Device added", device)
            auto_mount("/dev/" + device.sys_name)
            mp = get_mount_point("/dev/" + device.sys_name)
            print("Mount point: {}".format(mp))
            print_dev_stats(mp)
    return mp   

