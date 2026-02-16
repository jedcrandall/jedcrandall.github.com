
import math
import random
import ipaddress

p = (1 << 32) + 15

def factorsof(n):
    factors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n / i))
    return factors

print("p is " + str(p))
print(math.ceil(math.sqrt(p - 1)))
pminusonefactors = factorsof(p - 1)
print(pminusonefactors)

while True:
    root = random.randint(2, p - 2)
    rootfactors = factorsof(root)
    intersection = [x for x in rootfactors if x in pminusonefactors]
    if len(intersection) > 1:
        break

randip = random.randint(1, 1 << 32 - 1)

for i in range(65536): #1 << 32):
    randip = (randip * root) % p
    if randip < (1 << 32):
        ip_addr_obj = ipaddress.ip_address(randip)
        print(ip_addr_obj)
        

