import pyautogui as pyt
import time
import pyperclip as ppc

pyt.pause = 1

# script para automatizar o acesso a uma pagina de e-mail este era para o office365
pyt.hotkey("Win","r") # comando para abrir o executar do windows
pyt.write("chrome") # escreve o nome do programa
pyt.press("enter") # aperta a tecla enter
time.sleep(3) # comando para fazer uma interrupção maior de tempo. neste caso 3 segundo
ppc.copy("www.portal_que_desejamos_acessar.com.br")
pyt.hotkey("ctrl","v")
pyt.press("enter")
time.sleep(3)
pyt.write("login do usuarios")
pyt.press("enter")
time.sleep(5)
pyt.press("enter")
time.sleep(5)
ppc.copy("senha do usuario")
pyt.hotkey("ctrl","v")
pyt.press("enter")
time.sleep(3)
pyt.press("esc")
time.sleep(3)
pyt.press("tab")
pyt.press("tab")
pyt.press("enter")
