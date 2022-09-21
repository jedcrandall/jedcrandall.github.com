import random

printme = ''

for i in range(6):
    printme += chr(ord('0') + random.randint(0, 9))

print(printme)

