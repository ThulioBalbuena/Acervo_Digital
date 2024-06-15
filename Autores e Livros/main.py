from db.connection import Neo4jConnection
from models.autor import Autor
from models.livro import Livro

def menu():
    conn = Neo4jConnection("bolt://44.201.35.42:7687", "neo4j", "lumber-carbons-clerk")
    while True:
        print("1. Criar Livro")
        print("2. Ler Livro")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Criar Autor")
        print("6. Ler Autor")
        print("7. Atualizar Autor")
        print("8. Deletar Autor")
        print("9. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            titulo = input("Título do Livro: ")
            ano = input("Ano do Livro: ")
            genero = input("Gênero do Livro: ")
            numero_paginas = int(input("Número de Páginas do Livro: "))
            autor_nome = input("Nome do Autor do Livro: ")            
            verificar = Autor.ler(conn, autor_nome)
            if verificar == "Autor não encontrado.":
                print("Autor não encontrado.")
                print("Crie o autor antes de criar o livro.")
                idade = int(input("Idade do Autor (nome previamente inserido): "))
                autor = Autor(autor_nome, idade)
                autor.criar(conn)
                print("Autor criado com sucesso!") 
            
            livro = Livro(titulo, ano, genero, numero_paginas)
            livro.criar(conn)
            print("Livro criado com sucesso!")
            Autor.adicionar_livro(conn, autor_nome, titulo)
            print("Livro adicionado ao acervo do autor com sucesso")
        
        elif escolha == '2':
            titulo = input("Título do Livro: ")
            result = Livro.ler(conn, titulo)
            print(result)
        
        elif escolha == '3':
            titulo = input("Título do Livro: ")
            novo_titulo = input("Novo Título do Livro: ")
            novo_ano = input("Novo Ano do Livro: ")
            novo_genero = input("Novo Gênero do Livro: ")
            novo_numero_paginas = int(input("Novo Número de Páginas do Livro: "))
            Livro.atualizar(conn, titulo, novo_titulo, novo_ano, novo_genero, novo_numero_paginas)
            print("Livro atualizado com sucesso!")
        
        elif escolha == '4':
            titulo = input("Título do Livro: ")
            Livro.deletar(conn, titulo)
            print("Livro deletado com sucesso!")
        
        elif escolha == '5':
            nome = input("Nome do Autor: ")
            idade = int(input("Idade do Autor: "))
            autor = Autor(nome, idade)
            autor.criar(conn)
            print("Autor criado com sucesso!")
        
        elif escolha == '6':
            nome = input("Nome do Autor: ")
            result = Autor.ler(conn, nome)
            print(result)
        
        elif escolha == '7':
            nome = input("Nome do Autor: ")
            novo_nome = input("Novo Nome do Autor: ")
            nova_idade = int(input("Nova Idade do Autor: "))
            Autor.atualizar(conn, nome, novo_nome, nova_idade)
            print("Autor atualizado com sucesso!")
        
        elif escolha == '8':
            nome = input("Nome do Autor: ")
            Autor.deletar(conn, nome)
            print("Autor deletado com sucesso!")
        
        elif escolha == '9':
            conn.close()
            break
        
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

