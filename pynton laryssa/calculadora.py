numero1 = int(input("entre com numero1:"))
numero2 = int(input("entre com numero2:"))
op = int(input("entre com 1 soma, 2 multiplicacao, 3 dividir, 4 subtracao:"))
if op == 1:
    resul = numero1 + numero2
elif op == 2:
    resul = numero1 * numero2
elif op == 3:
    resul = numero1 / numero2
else:
    resul = numero1 - numero2
print(resul)
