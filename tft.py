import pyautogui 
import time

'''cord_x, cord_y = pyautogui.position()
print(str(cord_x)+";"+str(cord_y)) #900;770tft queue
'''
ciclo=0
while ciclo <3000:
    cord_x, cord_y = pyautogui.position()
    print(str(cord_x)+";"+str(cord_y)) #900;770 100% tft entrar queue 655;805 150%
    #969,673 100%,  771;679 150% aceptar cola
    #832,540 salir tft
    pyautogui.moveTo(655,805,1)#mover a buscar cola
    print(str(cord_x)+";"+str(cord_y)+" Moviendo a buscar cola") 
    pyautogui.click() #clickar buscar cola
    pyautogui.moveTo(771,679,1)#mover a aceptar cola
    print(str(cord_x)+";"+str(cord_y)+" Moviendo a Aceptar cola") 
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9)
    pyautogui.click()
    time.sleep(9) 

    time.sleep(60)#tuempo que dura el tft para ff en segundos
    cord_x, cord_y = pyautogui.position()
    pyautogui.moveTo(655,805,1)#mover a buscar cola
    print(str(cord_x)+";"+str(cord_y)+" Moviendo a buscar cola") 
    pyautogui.click() #clickar buscar cola
    ciclo=ciclo+1 
    print(ciclo)