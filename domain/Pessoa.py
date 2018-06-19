class Pessoa:

    def __init__(self, login, email, senha, id_pessoa=None):
        self.login = login
        self.email = email
        self.senha = senha
        self.id_pessoa = id_pessoa

    @property
    def id_pessoa(self):
        return self.id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        self.id_pessoa = id_pessoa

    @property
    def login(self):
        return self.login

    @login.setter
    def login(self, login):
        self.login = login

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def senha(self):
        return self.senha

    @email.setter
    def senha(self, senha):
        self.senha = senha