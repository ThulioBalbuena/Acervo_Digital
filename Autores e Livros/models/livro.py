class Livro:
    def __init__(self, titulo, ano, genero, numero_paginas):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.numero_paginas = numero_paginas

    def criar(self, conn):
        query = """
        CREATE (l:Livro {titulo: $titulo, ano: $ano, genero: $genero, numero_paginas: $numero_paginas})
        """
        conn.query(query, {
            'titulo': self.titulo, 
            'ano': self.ano,
            'genero': self.genero,
            'numero_paginas': self.numero_paginas
        })

    def ler(conn, titulo):
        query = """
        MATCH (l:Livro {titulo: $titulo})
        OPTIONAL MATCH (l)<-[:ESCREVEU]-(a:Autor)
        RETURN l.titulo AS titulo, l.ano AS ano, l.genero AS genero, l.numero_paginas AS numero_paginas, a.nome AS autor
        """
        result = conn.query(query, {'titulo': titulo})
        if result:
            titulo = result[0]["titulo"]
            ano = result[0]["ano"]
            genero = result[0]["genero"]
            numero_paginas = result[0]["numero_paginas"]
            autor = result[0]["autor"] or "Autor desconhecido"
            return f"--------\nInformações:\nTítulo: {titulo}\nAno: {ano}\nGênero: {genero}\nNúmero de Páginas: {numero_paginas}\nAutor: {autor}\n--------"
        else:
            return "Livro não encontrado."

    def atualizar(conn, titulo, novo_titulo, novo_ano, novo_genero, novo_numero_paginas):
        query = """
        MATCH (l:Livro {titulo: $titulo})
        SET l.titulo = $novo_titulo, l.ano = $novo_ano, l.genero = $novo_genero, l.numero_paginas = $novo_numero_paginas
        """
        conn.query(query, {
            'titulo': titulo, 
            'novo_titulo': novo_titulo, 
            'novo_ano': novo_ano,
            'novo_genero': novo_genero,
            'novo_numero_paginas': novo_numero_paginas
        })

    def deletar(conn, titulo):
        query = """
        MATCH (l:Livro {titulo: $titulo})
        DETACH DELETE l
        """
        conn.query(query, {'titulo': titulo})
