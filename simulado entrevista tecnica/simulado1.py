'''
🧠 EXERCÍCIO 1 — CONTAGEM
Você recebeu a seguinte lista de números:

[10, 5, 8, 10, 3, 5, 10]

TAREFA:

Crie uma função que:

Receba a lista

Retorne um dicionário informando quantas vezes cada número aparece

RESULTADO ESPERADO:
{10: 3, 5: 2, 8: 1, 3: 1}
'''

# lista de exemplo fornecida no enunciado
lista = [10, 5, 8, 10, 3, 5, 10]

'''
Crie uma função que inicializa um dicionário vazio e, para 
cada elemento da lista passada como parâmetro, use esse 
elemento como chave no dicionário; se a chave já existir, 
incremente o valor associado a ela, caso contrário, 
crie a chave com valor inicial 1.
'''
def dicionario(valores):
    # 'contagem' vai armazenar o número de ocorrências por valor
    contagem = {}

    # percorre cada elemento da lista fornecida
    for i in valores:
        # imprime o estado atual do dicionário (útil para entender o processo)
        print(contagem)
        # se o valor já foi visto antes (já existe como chave), incrementa o contador
        if i in contagem:
            contagem[i] += 1
        else:
            # se for a primeira vez que aparece, cria a chave com valor 1
            contagem[i] = 1
    

    # retorna o dicionário final com as contagens
    return contagem

# chama a função com a lista exemplo e imprime o resultado final
print(dicionario(lista))

'''
O dicionário funciona como um acumulador de estado, onde 
cada chave representa um valor único da lista e o valor 
associado representa quantas vezes ele apareceu.
'''