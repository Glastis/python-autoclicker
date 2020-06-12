import pyautogui
from pynput.keyboard import *
import ctypes
from time import sleep

ctypes.windll.kernel32.SetConsoleTitleW("Autoclicker")

#  ======== settings ========
delay = 1  # in seconds
resume_key = Key.f1
pause_key = Key.f2
mouse_down = Key.f3
mouse_up = Key.f4
exit_key = Key.esc
#  ==========================

down = False
pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == mouse_down:
        pyautogui.mouseDown()
        print("[Down]")
    elif key == mouse_up:
        pyautogui.mouseUp()
        print("[Up]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by iSayChris, forked by Glastis")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume click spam")
    print("\t F2 = Pause click spam")
    print("\t F3 = Mouse down")
    print("\t F4 = Mouse up")
    print("-----------------------------------------------------")



def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
        else:
            sleep(delay)
    lis.stop()


if __name__ == "__main__":
    main()
