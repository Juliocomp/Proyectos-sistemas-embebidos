import pyudev
import time
import os
import vlc
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)

monitor.filter_by(subsystem='usb')
x= 0
def handle_usb_event(action,device):
        global x
        if action == 'add':
                print("dispositivo conectado")
                print(device)
                os.system('sudo mount -a')
                x = 1
        elif action  == 'remove':
                print("dispositivo desconectado")
                print(device)
                x = 0
observer= pyudev.MonitorObserver(monitor, handle_usb_event)
observer.start()
try:
        print("Esperando conexion de memoria")
        while True:
                if x == 0:
                        images_folder = '/home/jules'
                if x == 1:
                        os.system('sudo mount -a')
                        images_folder = '/media/USBDRIVE'
                images = [os.path.join(images_folder, img) for img in os.listdir(images_folder) if img.endswith((".jpg", ".png"))]
                for image in images:
                        player=vlc.MediaPlayer(image)
                        player.play()
                        time.sleep(3)
                        player.stop()
except KeyboardInterrupt:
        observer.stop()
