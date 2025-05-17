#crear una funcion recursiva que me de la resta de la suma de los pares menos los impares de una lista

def r_p_i_recur(arr):
    if arr == []:
        return 0
    
    if arr[0] % 2 == 0:
        return arr[0] + r_p_i_recur(arr[1:])
    else: 
        return - arr[0] + r_p_i_recur(arr[1:])
    
lista1 = [5, 8, 1, 2]

z = r_p_i_recur(lista1)

print(f"El total de la resta es: {z}")


