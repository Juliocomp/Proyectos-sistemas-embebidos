
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
                time.sleep(3)
                player.stop()


def reproducir_musica(music_path):
        #player = vlc.MediaPlayer(music_path)
        #player.play()
        #while True:
        #        pass
        for song in music_path:
                player=vlc.MediaPlayer(song)
                player.play()
                time.sleep(3)
                player.stop()

def reproducir_video(video):
        media = vlc.Media(video)
        media_player.set_media(media)
        media_player.play()





def main_vlc():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem="block", device_type="partition")
    #while True:


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



    if any(file.endswith((".jpg", ".png")) for file in os.listdir(mp)):
            fotos = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".jpg", ".png"))]
            reproducir_presentacion(fotos)


    elif any(file.endswith((".mp3", ".wav")) for file in os.listdir(mp)):
            music = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".mp3", ".wav"))]
            if music:
                    reproducir_musica(music[0])
