import random
import time

bienvenida = "\nBienvenido a piedra, papel o tijera, espero que disfrutes!"

print(bienvenida)

op = ["piedra","papel","tijera"]

while True:
    user = input("\nElige la opcion: ").lower()
    time.sleep(0.5)
    if user not in op:
        print("No elegiste ninguna de las opciones, vuelve a intentarlo.")
        continue
    pc = random.choice(op)
    
    print(f"\nYo elegí: {pc}")
    
    time.sleep(0.5)
    
    if user == pc:
        print(f"\nEmpate, ambos elegimos: {user}")
    elif user == "tijera" and pc == "papel":
        print(f"\nGanaste eligiendo esa opción, yo elegí: {pc}")
    elif user == "papel" and pc == "tijera":
        print(f"\nGané, yo elegí: {pc}")
    elif user == "tijera" and pc == "piedra":
        print(f"\nGané, yo elegí: {pc}")
    elif user == "piedra" and pc == "tijera":
        print(f"\nGanaste eligiendo esa opción, yo elegí: {pc}")
    elif user == "papel" and pc == "piedra":
        print(f"\nGanaste eligiendo esa opción, yo elegí: {pc}")
    elif user == "piedra" and pc == "papel":
        print(f"\nGané, yo elegí: {pc}")
        time.sleep(0.5)
    else:
        print(f"\nPerdiste, {user} pierde contra {pc}")
        time.sleep(0.5)
    print("\n------------------- FIN DEL JUEGO! ---------------------")
    time.sleep(0.5)
    