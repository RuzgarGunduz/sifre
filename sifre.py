import random

sifre="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


soru=int(input("sifre uzunluğu ne olsun"))
sifreler=""
for i in range(soru):
    sifreler+=random.choice(soru)
print("sifreniz",sifreler)
