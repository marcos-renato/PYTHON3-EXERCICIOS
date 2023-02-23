from selenium import webdriver as web
import time  
from selenium.webdriver.common.alert import Alert



nav = web.Chrome()
nav.get('http://172.18.2.246:8090/scriptcase/app/ANS/blank_gerenciador_impressao/?nmgp_outra_jan=true&nmgp_start=SC&5032')

##t=True
##while t :
time.sleep(2)
nav.find_element("id","imprimir").click()
time.sleep(2)
dir(nav.window_handles())

##time.sleep(8)
##nav.refresh()