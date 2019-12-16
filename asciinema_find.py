import pyautogui
import time

startup = 5
pause = 0.5
secs_between_keys = 0.002

def atype(sentence):
    pyautogui.typewrite(sentence, interval=secs_between_keys)
    pyautogui.hotkey("enter")


if __name__ == '__main__':
    time.sleep(startup)
    atype("asciinema rec")
    pyautogui.hotkey("ctrl", "l")
    time.sleep(pause)
    atype(" # Searching for files does not need to be tedious")
    time.sleep(pause)
    atype(" # Say we want to find all files of the form favicon*png")
    time.sleep(pause)
    atype('fd "favicon.*png"')
    time.sleep(pause)

    atype(" # What if we want to search based on the contents of a file")
    time.sleep(pause)
    atype(" # Let's find all python files where we used the request package")
    time.sleep(1)
    atype('rg -t py "import requests" ')
    time.sleep(pause)
    pyautogui.hotkey("ctrl", "d")
    # pyautogui.hotkey("ctrl", "c")

