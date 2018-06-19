import sqlite3
from domain import Pessoa

class Conexao:

    def getCon(self):
        try:
            con = self.criarBanco()
            return con
        except Exception as e:
            print('Não foi possível criar a conexão\nErro: ',e)

    def criarBanco(self):
        try:
            con = sqlite3.connect(r'dados.db')
            cursor = con.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pessoa (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL,
                    email TEXT,
                    senha TEXT
                );
            """)
            return con;
        except Exception as e:
            print('erro: %s' %e)


class Dados(Conexao):

    def __init__(self):
        self.con = super().getCon()

    def novo(self):
        self.con.cursor().execute("insert into pessoa (login) values('Igor')")
        self.con.commit()

    def apagar(self, id_pessoa):
        self.con.cursor().execute(
            "delete from pessoa where id = ?",
            (id_pessoa,))
        self.con.commit()

    def atualizar(self, pessoa):
        pass

    def todos(self):
        pessoas = []
        lista = self.con.cursor().execute("select * from contato")
        for p in lista:
            pessoas.append(Pessoa.Pessoa(p[1],p[2],p[0]))

        return pessoas

    def pesquisar(self, nome):
        pessoas = []
        lista = self.con.cursor().execute("select * from contato where nome like ?",
                                          ('%'+str(nome)+'%',))
        for p in lista:
            pessoas.append(Pessoa.Pessoa(p[1],p[2],p[0]))

        return pessoas