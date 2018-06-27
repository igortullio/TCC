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
            con = sqlite3.connect('dados.db')
            cursor = con.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pessoa (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL,
                    senha TEXT,
                    email TEXT
                );
            """)
            return con;
        except Exception as e:
            print('erro: %s' %e)


class Dados(Conexao):

    def __init__(self):
        self.con = super().getCon()

    def novo(self, login, senha, email):
        self.con.cursor().execute("insert into pessoa(login, senha, email) values(?, ?, ?)", (login, senha, email))
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
		
    def login(self, login_, senha_):
        var_select = []
        var_select.append(login_)
        var_select.append(senha_)
        con = sqlite3.connect('dados.db')
        cursor = con.cursor()
        sql = 'SELECT * FROM pessoa WHERE login = ? AND senha = ?';
        cursor.execute(sql, var_select)
        result = cursor.fetchall()
        for row in result:
            print ("Login Válido")
            return True
