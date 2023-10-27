import random
refrigerios=[]

for _ in range(3000):
    liquidos=random.choice(['leche','agua','jugo','agua-saborisada'])
    comida=random.choice(['ponque','papas','sandwitch'])
    precios=random.randint(15000,40000)
    merienda=[liquidos,comida,precios]
    refrigerios.append(merienda)
    
print (refrigerios)