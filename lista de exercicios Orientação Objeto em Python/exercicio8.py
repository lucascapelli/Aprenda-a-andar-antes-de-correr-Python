class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_dados(self):
        return f"dados do produto, nome: {self.nome} preço: {self.preco:.2f} quantidade: {self.quantidade}"
    
    def atualizar_preco(self,novo_preco):
        self.preco = novo_preco
        return f"o novo preço do produto {self.nome} é: {self.preco:.2f} R$"
    
    def adicionar_estoque(self,qtd):
        self.quantidade += qtd
        return f"agora a quantidade em estoque de {self.nome} é de: {self.quantidade}"
    
    def retirar_estoque(self, qtd):
        if self.quantidade < qtd:
            return f"você tem em estoque uma quantidade menor do que está tentando retirar"
        else:
            self.quantidade -= qtd
        return f"agora você tem em estoque: {self.quantidade}"
        
wheyprotein = Produto('growth - wheyprotein', 89.99 , 450)

print(wheyprotein.retirar_estoque(1000))