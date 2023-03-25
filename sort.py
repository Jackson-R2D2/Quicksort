def sort(array = []):
    if len(array) < 2:
        return array
    meio = array[0]
    lista_maior = sort([valor for valor in array[1:] if valor > meio])
    lista_menor = sort([valor for valor in array[1:] if valor <= meio])
    lista_menor.append(meio)
    return lista_menor + lista_maior

print(sort([1,2,6,5,7,9,4,10,3,8,8,1,10,12,-1,15]))
