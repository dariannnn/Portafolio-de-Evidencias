import pyautogui,time
from faker import Faker
faker = Faker()

frase1 = input("Escriba un refrán, catchphrase, dicho popular o cita de libro o película: ")
frase2 = input("Escriba un refrán, catchphrase, dicho popular o cita de libro o película (segundo llenado): ")

cor1 = faker.email()
cor2 = faker.email()

formData = [{'opcion': 'Marvel', 'frase': frase1, 'hora': '8', 'correo': cor1},
            {'opcion': 'DC', 'frase': frase2, 'hora': '9', 'correo': cor2},
            ]

print("Comenzando proceso de llenado")
for vuelta in formData:
    time.sleep(5)

    # Pregunta 1
    if vuelta['opcion'] == 'Marvel':
        pyautogui.click(x=361, y = 462, clicks = 1)
        pyautogui.press('enter')
        pyautogui.press('tab')
    elif vuelta['opcion'] == 'DC':
        pyautogui.click(x=362, y = 498, clicks = 1)
        pyautogui.press('enter')
        pyautogui.press('tab')
    
    # Pregunta 2
    pyautogui.typewrite(vuelta['frase'])
    pyautogui.press('tab')

    # Pregunta 3
    if vuelta['hora'] == '8':
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('tab')
    elif vuelta['hora'] == '9':
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')

    # Pregunta 4
    pyautogui.typewrite(vuelta['correo'])
    pyautogui.press('tab')

    # Submit
    pyautogui.press('enter')
    print('Submit.')
    time.sleep(5)

    # Submit another response
    pyautogui.click(x=450, y = 470, clicks = 1)


# Para propósito de llenar tabla de entregables
for vuelta in formData:            
    for x, y in vuelta.items():
        print(x, ":",y)
    print("\n")
    
