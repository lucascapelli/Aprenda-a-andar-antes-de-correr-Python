class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:  # Verifica se pode emprestar
            self.disponivel = False # se true muda pra false, se already false vai pro segundo return
            return f"{self.titulo} eu te empresto emprestado."
        return f"{self.titulo} já está emprestado!"

    def devolver(self):
        self.disponivel = True
        return f"{self.titulo} foi devolvido."

class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista vazia pra guardar os livros
    
    def adicionar_livro(self, livro):  # Adiciona um livro à lista
        self.livros.append(livro)
    
    def mostrar_disponiveis(self):  # Mostra livros disponíveis
        disponiveis = [livro.titulo for livro in self.livros if livro.disponivel]
        if disponiveis:
            return "Livros disponíveis: " + ", ".join(disponiveis)
        return "Nenhum livro disponível."

# Testando
biblia = Livro("Bíblia", "Deus")
harry_potter = Livro("Harry Potter", "J.K. Rowling")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(biblia)
biblioteca.adicionar_livro(harry_potter)

print(biblioteca.mostrar_disponiveis())  # Saída: Livros disponíveis: Bíblia, Harry Potter
print(biblia.emprestar())                # Saída: Bíblia foi emprestado.
print(biblioteca.mostrar_disponiveis())  # Saída: Livros disponíveis: Harry Potter
print(biblia.emprestar())                # Saída: Bíblia já está emprestado!
print(biblia.devolver())                 # Saída: Bíblia foi devolvido.
print(biblioteca.mostrar_disponiveis())  # Saída: Livros disponíveis: Harry Potter, Bíblia

input()