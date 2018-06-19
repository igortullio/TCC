class Cadeira:

    def __init__(self, status, id_cadeira=None):
        self.status = status
        self.id_cadeira = id_cadeira

    @property
    def id_cadeira(self):
        return self.id_cadeira

    @id_cadeira.setter
    def id_cadeira(self, id_cadeira):
        self.id_cadeira = id_cadeira

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        self.status = status
