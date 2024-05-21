
import subprocess
import curses
#from detecusb import *
from montar_usb import *



def mostrar_menu(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Bienvenido al centro de entretenimiento: ", curses.A_BOLD)
        stdscr.addstr(2, 0, "1. Servicios en linea para video")
        stdscr.addstr(3, 0, "2. Servicios en linea para musica")
        stdscr.addstr(4, 0, "3. Reproducir desde medio extraible")
        stdscr.addstr(5, 0, "Selecciona una opcion: ")
        stdscr.refresh()
        opcion = stdscr.getch()
        return opcion



def mostrar_submenu_video(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "seleccione un servicio en linea para streaming", curses.A_BOLD)
        stdscr.addstr(2, 0, "1. Netflix")
        stdscr.addstr(3, 0, "2. Prime Video")
        stdscr.addstr(4, 0, "3. Vix")
        stdscr.refresh()
        opcion = stdscr.getch()
        return opcion

def mostrar_submenu_musica(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Seleccione un servicio en linea para musica", curses.A_BOLD)
        stdscr.addstr(2, 0, "1. Spotify")
        stdscr.addstr(3, 0, "2. Deezer")
        stdscr.addstr(4, 0, "3. Amazon music")
        stdscr.refresh()
        opcion = stdscr.getch()
        return opcion

def abrir_netflix(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Abriendo Netflix en el navegador... presiona Enter", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        subprocess.run(["startx","/bin/chromium-browser", "https://www.netflix.com"])

def abrir_prime_video(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Abriendo Amazon Prime Video en el navegador... presiona Enter", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        subprocess.run(["startx", "/bin/chromium-browser", "https://www.primevideo.com"])

def abrir_vix(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Abriendo Vix en el navegador... presiona Enter", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        subprocess.run(["startx", "/bin/chromium-browser", "https://www.vix.com/es"])

def abrir_spotify(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Abriendo spotify en el navegador... presiona Enter", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        subprocess.run(["startx", "/bin/chromium-browser", "https://www.spotify.com"])

def abrir_deezer(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Abriendo deezer en el navegador... presiona Enter")
        stdscr.refresh()
        stdscr.getch()
        subprocess.run(["startx", "/bin/chromium-browser", "https://www.deezer.com"])

def abrir_amazon_music(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Abriendo Amazon music en el navegador... presiona Enter", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        subprocess.run(["startx", "/bin/chromium/browser", "https://music.amazon.com"])

def mostrar_mensaje(stdscr, opcion_elegida):
        numero_arch=None
        if opcion_elegida == ord('1'):
                subopcion_elegida = None
                while subopcion_elegida not in [ord('1'), ord('2'), ord('3'), ord('8')]:
                        subopcion_elegida = mostrar_submenu_video(stdscr)
                        if subopcion_elegida == ord('1'):
                                abrir_netflix(stdscr)
                        elif subopcion_elegida == ord('2'):
                                abrir_prime_video(stdscr)
                        elif subopcion_elegida == ord('3'):
                                abrir_vix(stdscr)
        elif opcion_elegida == ord('2'):
                subopcion_elegida = None
                while subopcion_elegida not in [ord('1'), ord('2'), ord('3'), ord('8')]:
                        subopcion_elegida =  mostrar_submenu_musica(stdscr)
                        if subopcion_elegida == ord('1'):
                                abrir_spotify(stdscr)
                        elif subopcion_elegida == ord('2'):
                                abrir_deezer(stdscr)
                        elif subopcion_elegida == ord('3'):
                                abrir_amazon_music(stdscr)

        elif opcion_elegida == ord('3'):
                subopcion_elegida=None
                mp=''
                print("\n Por favor conecte una usb")
                mp=main_vlc()
                """
                fotos=int(len(numero_arch[0]))
                videos=int(len(numero_arch[1]))
                if fotos>0 and videos>0:
                        print("Seleccione un tipo de archivo para desplegar")
                elif fotos>0:
                        print("Se van a desplegar las fotos")
                elif videos>0:
                        print("se van a desplegar videos")
                """
                medios=[]
                if any(file.endswith((".jpg", ".png")) for file in os.listdir(mp)):
                        medios.append("imagenes")
                if any(file.endswith((".mp3", ".wav")) for file in os.listdir(mp)):
                        medios.append("audio")
                if any(file.endswith((".mp4", ".avi")) for file in os.listdir(mp)):
                        medios.append("video")


                if len(medios)==0:
                        print("NINGUNO DE LOS FORMATOS ES REPRODUCIBLE")
                elif len(medios)==1:
                        if medios[0]=="imagenes":
                                fotos = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".jpg", ".png"))]
                                reproducir_presentacion(fotos)


                        elif medios[0]=="audio":
                                music = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".mp3", ".wav"))]
                                if music:
                                        reproducir_musica(music)
                        elif medios[0]=="video":
                                #video = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".mp4", ".avi"))]
                                #reproducir_video(video)
                                medios = [f for f in os.listdir(mp) if f.endswith((".mp4", ".avi"))]
                                stdscr.addstr(0, 0, "Seleccione el video que quiere ver:")
                                for i, medio in enumerate(medios):
                                        stdscr.addstr(i+1, 0, f"{i+1}. {medio}")

                                selection = 0
                                selected_option = None  # Variable para guardar la opción seleccionada

                                # Maneja las teclas de flecha hacia arriba y hacia abajo
                                key = stdscr.getch()
                                while True:  # Mantén el menú abierto hasta que se presione Enter
                                        if key == curses.KEY_UP and selection > 0:
                                                selection -= 1
                                        elif key == curses.KEY_DOWN and selection < len(medios) - 1:
                                                selection += 1
                                        elif key == curses.KEY_ENTER or key in [10, 13]:  # Valores ASCII para Enter
                                                selected_option = medios[selection]
                                                stdscr.addstr(1, 0, f"\nHas seleccionado: {selected_option}\n")  # Muestra la opción seleccionada
                                                stdscr.refresh()  # Asegura que el mensaje se muestre en la pantalla
                                                stdscr.getch()  # Espera a que el usuario presione cualquier tecla para continuar
                                                reproducir_video(os.path.join(mp, selected_option))

                                                break  # Finaliza el bucle para salir del menú

                                        # Actualiza la selección mostrada
                                        stdscr.clear()
                                        stdscr.addstr(0, 0, "Seleccione el video que quiere ver:")
                                        for i, medio in enumerate(medios):
                                                if i == selection:
                                                        stdscr.addstr(i+1, 0, f"> {i+1}. {medio}")  # Resalta la opción seleccionada
                                                else:
                                                        stdscr.addstr(i+1, 0, f"  {i+1}. {medio}")

                                        stdscr.refresh()  # Refresca la pantalla
                                        key = stdscr.getch()


                elif len(medios)>1:

                        stdscr.addstr(0, 0, "La memoria puede reproducir archivos de tipo:")
                        for i, medio in enumerate(medios):
                                stdscr.addstr(i+1, 0, f"{i+1}. {medio}")

                        selection = 0
                        selected_option = None  # Variable para guardar la opción seleccionada

                        # Maneja las teclas de flecha hacia arriba y hacia abajo
                        key = stdscr.getch()
                        while True:  # Mantén el menú abierto hasta que se presione Enter
                                if key == curses.KEY_UP and selection > 0:
                                        selection -= 1
                                elif key == curses.KEY_DOWN and selection < len(medios) - 1:
                                        selection += 1
                                elif key == curses.KEY_ENTER or key in [10, 13]:  # Valores ASCII para Enter
                                        selected_option = medios[selection]
                                        stdscr.addstr(1, 0, f"\nHas seleccionado: {selected_option}\n")  # Muestra la opción seleccionada
                                        stdscr.refresh()  # Asegura que el mensaje se muestre en la pantalla
                                        stdscr.getch()  # Espera a que el usuario presione cualquier tecla para continuar
                                        if selected_option=="imagenes":
                                                fotos = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".jpg", ".png"))]
                                                reproducir_presentacion(fotos)


                                        elif selected_option=="audio":
                                                music = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".mp3", ".wav"))]
                                                if music:
                                                        reproducir_musica(music[0])
                                        elif selected_option=="video":
                                #video = [os.path.join(mp, f) for f in os.listdir(mp) if f.endswith((".mp4", ".avi"))]
                                #reproducir_video(video)
                                                medios_v = [f for f in os.listdir(mp) if f.endswith((".mp4", ".avi"))]
                                                stdscr.addstr(0, 0, "Seleccione el video que quiere ver:")
                                                for i, medio in enumerate(medios_v):
                                                        stdscr.addstr(i+1, 0, f"{i+1}. {medio}")

                                                selection = 0
                                                selected_option = None  # Variable para guardar la opción seleccionada

                                # Maneja las teclas de flecha hacia arriba y hacia abajo
                                                key = stdscr.getch()
                                                while True:  # Mantén el menú abierto hasta que se presione Enter
                                                        if key == curses.KEY_UP and selection > 0:
                                                                selection -= 1
                                                        elif key == curses.KEY_DOWN and selection < len(medios) - 1:
                                                                selection += 1
                                                        elif key == curses.KEY_ENTER or key in [10, 13]:  # Valores ASCII para Enter
                                                                selected_option = medios_v[selection]
                                                                stdscr.addstr(1, 0, f"\nHas seleccionado: {selected_option}\n")  # Muestra la opción seleccionada
                                                                stdscr.refresh()  # Asegura que el mensaje se muestre en la pantalla
                                                                stdscr.getch()  # Espera a que el usuario presione cualquier tecla para continuar
                                                                reproducir_video(os.path.join(mp, selected_option))

                                                                break  # Finaliza el bucle para salir del menú

                                        # Actualiza la selección mostrada
                                                        stdscr.clear()
                                                        stdscr.addstr(0, 0, "Seleccione el video que quiere ver:")
                                                        for i, medio in enumerate(medios_v):
                                                                if i == selection:
                                                                        stdscr.addstr(i+1, 0, f"> {i+1}. {medio}")  # Resalta la opción seleccionada
                                                                else:
                                                                        stdscr.addstr(i+1, 0, f"  {i+1}. {medio}")

                                                        stdscr.refresh()  # Refresca la pantalla
                                                        key = stdscr.getch()


                                        break  # Finaliza el bucle para salir del menú

                                # Actualiza la selección mostrada
                                stdscr.clear()
                                stdscr.addstr(0, 0, "La memoria puede reproducir archivos de tipo:")
                                for i, medio in enumerate(medios):
                                        if i == selection:
                                                stdscr.addstr(i+1, 0, f"> {i+1}. {medio}")  # Resalta la opción seleccionada
                                        else:
                                                stdscr.addstr(i+1, 0, f"  {i+1}. {medio}")

                                stdscr.refresh()  # Refresca la pantalla
                                key = stdscr.getch()
##############################


        elif opcion_elegida == ord('8'):
                return False
        else:
                stdscr.clear()
                stdscr.addstr(0, 0, f"Ha seleccionado la opcion : {chr(opcion_elegida)}")
                stdscr.refresh()
                stdscr.getch()
        return True

def main(stdscr):
        curses.curs_set(0)
        opcion_elegida = None
        while opcion_elegida != ord('8'):
                opcion_elegida = mostrar_menu(stdscr)
                if not mostrar_mensaje(stdscr, opcion_elegida):
                        break
if __name__=="__main__":
        curses.wrapper(main)







