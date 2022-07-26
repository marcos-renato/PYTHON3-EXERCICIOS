import pyautogui as pyt
import time
import pyperclip as ppc

pyt.pause = 1

##pyt.alert("Vai começar, aperte ok e não mexa em nada")
##time.sleep = 2
pyt.hotkey("Win","r")
pyt.write("chrome")
pyt.press("enter")
time.sleep(3)
ppc.copy("portal.office.com")
pyt.hotkey("ctrl","v")
pyt.press("enter")
time.sleep(3)
pyt.write("marcos.vicente@santacasajf.org.br")
pyt.press("enter")
time.sleep(5)
pyt.press("enter")
time.sleep(5)
ppc.copy("F@b14n4M4rt1ns")
pyt.hotkey("ctrl","v")
pyt.press("enter")
time.sleep(3)
pyt.press("esc")
time.sleep(3)
pyt.press("tab")
pyt.press("tab")
pyt.press("enter")
