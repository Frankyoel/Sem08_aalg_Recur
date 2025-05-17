def ite():
    x = 1
    while True:
        print("hola amigos")
        x=+1

def recur(x,n):
    if x == n:
        print("Se termino el ciclo")
    else:
        print(f"bienvenido nro {x}")
        recur(x+1, n)


def recur2(x):
    if x == 0:
        print("Se termino el ciclo")
    else:
        print(f"bienvenido nro {x}")
        recur2(x-1)

#---------------------------#

#ite()
recur2(10)

