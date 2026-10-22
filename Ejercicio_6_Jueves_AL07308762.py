print("\n============================================")
print("Ejercicio 6: Vidas y daño")
print("========================== BATALLA =========")
#Damos de alta la variable personaje y vida
personaje = "Bmax"
vida = 100
print(f"\nMi personaje se llama {personaje} y empieza con {vida} de vida")
#Como vida vale 100, esta formula dice: vida = 100 -30
vida = vida -30
print(f"Me dio un golpe de un goblin, ahora tengo vida: {vida}")
#Ahora vida vale 70, esta formula dice: vida = 100 - 30
vida = vida - 30
print(f"Ah, ahora me toco el golpe de un ogro, tengo de vida {vida}")
#Ahora vida vale 30, esta formula dice: vida = 35 - 15
#vida = vida - 15 
print(f"Me toco una flecha enemiga!, tengo de vida: {vida}") 
#Ahora vida vale 20, esta formula dice: vida = 20 + 20
vida = vida + 40
print(f"Tomó una opción... mi vida: {vida}")

print(f"\n{personaje} terminó la batalla con {vida} HP\n")
print("============================================================")