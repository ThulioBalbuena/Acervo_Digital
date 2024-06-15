class Autor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def criar(self, conn):
        query = """
        CREATE (a:Autor {nome: $nome, idade: $idade})
        """
        conn.query(query, {'nome': self.nome, 'idade': self.idade})

    def ler(conn, nome):
        query = """
        MATCH (a:Autor {nome: $nome})
        OPTIONAL MATCH (a)-[:ESCREVEU]->(l:Livro)
        RETURN a.nome AS nome, a.idade AS idade, collect(l.titulo) AS livros
        """
        result = conn.query(query, {'nome': nome})
        if result:
            nome = result[0]["nome"]
            idade = result[0]["idade"]
            livros = result[0]["livros"]
            if livros:
                livros = sorted(livros)
                livros_str = "\n".join(livros)
            else:
                livros_str = "Nenhum livro encontrado"
            return f"--------\nInformações:\nNome: {nome}\nIdade: {idade}\nLivros:\n{livros_str}\n--------"
        else:
            return "Autor não encontrado."

    def atualizar(conn, nome, novo_nome, nova_idade):
        query = """
        MATCH (a:Autor {nome: $nome})
        SET a.nome = $novo_nome, a.idade = $nova_idade
        """
        conn.query(query, {'nome': nome, 'novo_nome': novo_nome, 'nova_idade': nova_idade})

    def deletar(conn, nome):
        query = """
        MATCH (a:Autor {nome: $nome})
        DETACH DELETE a
        """
        conn.query(query, {'nome': nome})

    def adicionar_livro(conn, nome_autor, titulo_livro):
        query = """
        MATCH (a:Autor {nome: $nome_autor}), (l:Livro {titulo: $titulo_livro})
        CREATE (a)-[:ESCREVEU]->(l)
        """
        conn.query(query, {'nome_autor': nome_autor, 'titulo_livro': titulo_livro})
