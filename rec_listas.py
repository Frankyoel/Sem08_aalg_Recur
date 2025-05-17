#haga una funcion que obtenga la suma de los elementos de un lista

def suma(arr, x) -> int:
    if x == 0:
        return arr[0]
    else:
        return arr[x] + suma(arr, x - 1)
        #print(arr.sort)

def sumlst(arr):
    arr2 = arr[0]

    if arr == []:
        return 0  
    else:
        arr + sumlst(arr2[1:])

lista1 = [5, 8, 6, 2]

z = suma(lista1, len(lista1) - 1)


#print(z)

y = sumlst(lista1)

print(y)