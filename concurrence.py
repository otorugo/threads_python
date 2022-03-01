from threading import Thread
from time import sleep, perf_counter

def sample_function(name : str):
    print(f"Seja Bem Vindo : {name}!")
    print("Seu pedido está sendo processado!")
    sleep(2)
    print(f"Pedido de {name} foi processado!")
    
list_names = ("Victor","Joãozin","Alguém")
s = perf_counter()
for names in list_names:
    
    t = Thread(target=sample_function,args=(names,))
    t.start()
    
elapsed = perf_counter() - s

print(f"O negocio durou {elapsed}")
