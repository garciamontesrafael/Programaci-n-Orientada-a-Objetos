print("--- IMC ---")
peso=int(input("Inserte su peso en Kg: "))
altura=float(input("Inserte su altura en metros: "))
imc=peso/altura**2

print(f"Tu IMC es: {imc}")

if imc <19.5:
    print("Estas bajo de peso")
elif imc < 25:
    print("Estas en un peso normal")
else:
    print("Tienes obecidad brou")