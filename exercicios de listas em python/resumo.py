# Criando uma lista
frutas = ["maçã", "banana", "uva"]

# Acessando elementos (índice começa do zero)
print(frutas[0])  # maçã

# Alterando valores
frutas[1] = "laranja"

# Adicionando elementos
frutas.append("abacaxi")

# Inserindo em posição específica
frutas.insert(1, "melancia")  # insere na posição 1

# Removendo elementos
frutas.remove("uva")          # remove pelo valor
del frutas[0]                 # remove pelo índice
frutas.pop()                  # remove o último

# Tamanho da lista
print(len(frutas))

# Verificar se algo está na lista
if "banana" in frutas:
    print("Tem banana!")

# Ordenar e inverter
frutas.sort()     # ordem alfabética
frutas.reverse()  # inverte a ordem

# Criando uma lista
frutas = ["maçã", "banana", "uva"]
print("Lista original:", frutas)

# append() - adiciona no final
frutas.append("abacaxi")
print("Depois do append('abacaxi'):", frutas)

# insert() - insere em posição específica
frutas.insert(1, "melancia")
print("Depois do insert(1, 'melancia'):", frutas)

# pop() - remove o último elemento e retorna ele
ultimo = frutas.pop()
print("Elemento removido com pop():", ultimo)
print("Depois do pop():", frutas)

# pop(indice) - remove um item pelo índice
removido = frutas.pop(1)
print("Elemento removido com pop(1):", removido)
print("Depois do pop(1):", frutas)

# remove(valor) - remove o primeiro valor igual
frutas.remove("banana")
print("Depois do remove('banana'):", frutas)

# del - remove um item pelo índice
del frutas[0]
print("Depois do del frutas[0]:", frutas)

# del - pode apagar a lista inteira
del frutas
# print(frutas)  # Isso daria erro, pois a lista foi deletada
