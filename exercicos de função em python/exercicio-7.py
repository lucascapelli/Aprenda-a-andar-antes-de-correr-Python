'''
✅ Função 1: calcular_desconto(preco, percentual)

    Recebe dois parâmetros:

        preco (valor original do produto)

        percentual (desconto em %)

    Retorna o valor do desconto (em reais).

✅ Função 2: preco_final(preco, desconto)

    Recebe:

        preco (valor original)

        desconto (valor do desconto em reais)

    Retorna o preço final (original - desconto), formatado para 2 casas decimais.

✅ Função 3: exibir_resumo(preco, percentual)

    Chama as duas funções anteriores internamente.

    Exibe:

Preço original: R$[preco]
Desconto: R$[desconto]
Preço final: R$[preco_final]

'''

def calcular_desconto(preco,percentual):
    desconto = (percentual/100) * preco
    return desconto


def preco_final(preco, desconto):
    precof = preco - desconto
    return precof



def exibir_resumo(preco,percentual):
    desconto_calculado = calcular_desconto(preco,percentual)
    preco_final_calculado = preco_final(preco,desconto_calculado)
    
    print (f'Preço original: R${preco}')
    print(f'Desconto do produto R${desconto_calculado:.2f}')
    print (f'Preço final do Produto R${preco_final_calculado:.2f}')

exibir_resumo(150,10)