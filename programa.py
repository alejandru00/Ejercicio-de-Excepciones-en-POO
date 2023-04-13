

import re

class Validar:
    def __init__(self, correo):
        self.correo = correo

    def validar_correo(self):
        validar = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.correo)

        #Comprobamos si la entrada no es vacía.
        if self.correo == "":
            print("'' es una entrada incorrecta. Introduzca una dirección de correo electrónico válida.")
            self.correo = input("-> ")
            self.validar_correo()
            

        #Comprobamos si el correo tiene el formato.
        elif validar:
            #Comprobamos si el correo ya existe.
            if self.correo in correos_existentes:
                print(f"La dirección de correo electrónico es válida. Bienvenido {self.correo}.")        #Damos la bienvenida si existe.
                pass

            else:
                print("Cuenta bloqueada a causa de un ataque.")                                          #Bloqueamos la cuenta si no existe.
                pass

        #Otros casos.
        else:
            print("La dirección de correo electrónico debe tener el formato xxx@xxx.xx .")
            self.correo = input("-> ")
            self.validar_correo()


correos_existentes = ["usuario1@gmail.com", "usuario2@yahoo.com"]       #Correos existentes.

correo = input("-> ")                                     
validar = Validar(correo) 
validar.validar_correo()                                                          