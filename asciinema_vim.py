import pyautogui
import time

startup = 5
pause = 0.5
secs_between_keys = 0.002

def atype(sentence):
    pyautogui.typewrite(sentence, interval=secs_between_keys)
    pyautogui.hotkey("enter")

def vtype(sentence):
    pyautogui.typewrite(sentence, interval=3*secs_between_keys)

if __name__ == '__main__':
    time.sleep(startup)
    atype("asciinema rec")
    pyautogui.hotkey("ctrl", "l")
    time.sleep(pause)
    atype(" # Text editors can deal with many tedious tasks")
    time.sleep(pause)
    atype(" # For instance, we can easily convert html tables to csv using vim macros")
    time.sleep(pause)
    atype('nvim table.html')
    time.sleep(pause)

    vtype('ggjj0')
    vtype('qadf>f<d$a,')
    pyautogui.hotkey("delete")
    pyautogui.hotkey("esc")
    vtype('lq3uggj')
    time.sleep(pause)
    vtype('qbdd0@a')
    time.sleep(0.2)
    vtype('@a')
    time.sleep(0.2)
    vtype('@ahd$jq')
    time.sleep(pause)
    vtype('@b')
    time.sleep(pause)
    vtype('5@b')
    time.sleep(pause)
    vtype('ddggdd')
    atype(':saveas table.csv')
    pyautogui.hotkey("enter")
    vtype('ZZ')


    atype(" # We made a macro for a line and then reused it for the entire block")
    time.sleep(pause)
    # atype(" # The entire vim sequence was ")
    # time.sleep(pause)
    # atype(" # jj0qadf>f<d$a,<DEL><ESC>lq3uggjqbdd03@ahd$jq6@bddggdd")
    time.sleep(pause)
    pyautogui.hotkey("ctrl", "d")
    # pyautogui.hotkey("ctrl", "c")

