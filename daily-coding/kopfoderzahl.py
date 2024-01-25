import random

def muenzwurf():
    rand_1 = random.randint(0,1)
    outcomes = ["Kopf","Zahl"]
    return outcomes[rand_1]
print(muenzwurf())