class Livro:
    def __init__(self,titulo,autor,ano_publicação,disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicação = ano_publicação
        self.disponivel = disponivel

    def exibir_dados(self):
        return f"livro: {self.titulo} autor: {self.autor} ano de publicação {self.ano_publicação}"
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f"o livro {self.titulo} está sendo emprestado para você, com um prazo de devolução de 15 dias"
        else:
            return f"infelizmente o livro {self.titulo} já foi emprestado"
        
    def devolver(self):
        # Se o livro NÃO/NOT está disponível (ou seja, está emprestado)...
        if not self.disponivel:
        # ...então marque como disponível (devolvido)...
            self.disponivel = True
        # ...e diga que ele está sendo devolvido
            return f"você está devolvendo o livro {self.titulo}"
        else:
        # Caso contrário, ele já está disponível (na biblioteca)
            return f"o livro {self.titulo} já está na biblioteca"
    
biblia = Livro('biblia','Deus',325,False)

print(biblia.exibir_dados())
print(biblia.emprestar())
print(biblia.devolver())