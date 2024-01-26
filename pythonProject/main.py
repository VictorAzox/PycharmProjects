numbers = [10, 23, 43, 54, 65, 64, 87, 43, 21, 11]

for numbers in numbers:
    if numbers%2 == 0:
        continue
    print(numbers)

'''
print("Contando de 0 a 9")
for i in range (10):
    print(i)'''

for i in range (1, 100, 2):
    print(i)
else:
    print('Reached to the limit')
