'''for numero in range(6):
    print(numero)
print("  ")
for numero in  range(1,5):
    print(numero)


for numero in range(1, 20, 2):
    print(numero)
'''
flagcompra = True
info = "Compra efetuada"
for tentativa in range(3):
    if flagcompra:
        print(info)
        break
else:
    print("Houve um problema na compra")

lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)

frutas1 = ["abacate", "banana", "morango"]
frutas2 = []

for fruta in frutas1:
    if 'n' in fruta:
        frutas2.append(fruta)
'''print(frutas2)'''

index= 0
frutas3 = [fruta for fruta in frutas1 if 'n' in fruta]
print(frutas3)

for fruta in frutas1:
    print(index,fruta)
    index +=1
for cont, fruta in enumerate (frutas1):
    print(cont, fruta)
