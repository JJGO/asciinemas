import pyautogui
import time

startup = 5
pause = 0.5
secs_between_keys = 0.002

def atype(sentence):
    pyautogui.typewrite(sentence, interval=secs_between_keys)
    pyautogui.hotkey("enter")

def btype(sentence):
    pyautogui.typewrite(sentence, interval=secs_between_keys)


if __name__ == '__main__':
    time.sleep(startup)
    atype("asciinema rec")
    pyautogui.hotkey("ctrl", "l")
    time.sleep(pause)
    atype(" # You can easily make use of the shell history to be more productive")
    time.sleep(pause)
    atype(" # I recently used a command to generate a bunch of favicons")
    time.sleep(pause)
    atype(" # Let's see how my shell automatically completes it")
    time.sleep(3*pause)
    btype("convert")
    time.sleep(pause)
    pyautogui.hotkey("right")
    pyautogui.hotkey("ctrl", "c")
    atype(" # We can also quickly navigate matching lines")
    btype("convert")
    for i in range(5):
        pyautogui.hotkey("up")
        time.sleep(0.3)
    pyautogui.hotkey("ctrl", "c")
    atype(" # Sometimes we need to match in a fuzzy way")
    time.sleep(pause)
    pyautogui.hotkey("ctrl", "r")
    btype("convert background")
    time.sleep(3*pause)
    pyautogui.hotkey("enter")
    pyautogui.hotkey("ctrl", "c")
    time.sleep(pause)
    pyautogui.hotkey("ctrl", "d")
    # pyautogui.hotkey("ctrl", "c")

