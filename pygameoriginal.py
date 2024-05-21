import os
import pyudev
import subprocess as sp
import vlc
import pygame
from pygame.locals import *

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
        print("funciona")
        pygame.init()
        screen = pygame.display.set_mode((0, 0), FULLSCREEN)
        pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()

        current_index = 0
        total_images = len(fotos)

        while True:
                for event in pygame.event.get():
                        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                                return
                image_path = fotos[current_index]
                imagen = pygame.image.load(image_path)
                imagen = pygame.transform.scale(imagen, screen.get_size())
                screen.blit(imagen, (0, 0))
                pygame.display.flip()

                current_index = (current_index + 1) % total_images
                clock.tick(2)
        pygame.quit()

def reproducir_musica(music_path):
        player = vlc.MediaPlayer(music_path)
        player.play()
        while True:
                pass

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem="block", device_type="partition")
while True:
        action, device = monitor.receive_device()
        if action != "add":
                continue
        print("Device added", device)
        auto_mount("/dev/" + device.sys_name)
        mp = get_mount_point("/dev/" + device.sys_name)
        print("Mount point: {}".format(mp))
        print_dev_stats(mp)
        if any(file.endswith((".jpg", ".png")) for file in os.listdir(mp)):
                fotos = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".jpg", ".png"))]
                reproducir_presentacion(fotos)
        elif any(file.endswith((".mp3", ".wav")) for file in os.listdir(mp)):
                music = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".mp3", ".wav"))]
                if music:
                        reproducir_musica(music[0])
