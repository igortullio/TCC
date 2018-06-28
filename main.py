from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
import sqlite3


class Home(Screen):
    pass


class Cadastro(Screen):

    def realizar_cadastro(self):
        Dados().novo(self.ids["ti_usuario"].text, self.ids["ti_senha"].text,
                     self.ids["ti_email"].text)  # método para cadastrar
        self.ids["lb_cadastro1"].text = "Cadastro realizado com sucesso"


class Mesas(Screen):

    def oi(self):
        for i in range(0, 35):
            self.ids["outros"].add_widget(Button(text="oi"))


class Login(Screen):

    def login_valido(self):
        if Dados().login(self.ids["ti_usuario"].text,
                         self.ids["ti_senha"].text):  # chamada método verificar login no banco
            return True
        # pass


class ScreenManagement(ScreenManager):

    def trocar_tela(self, tela):
        self.current = tela
        # pass


class Tela(App):

    def build(self):
        return presentation


presentation = Builder.load_file("tela.kv")
Window.size = 500, 600  # Window.size = 500, 800  #original

if __name__ == "__main__":
    from conection.Conexao import Dados

    Dados().getCon()  # criar banco
    Tela().run()

#: import FadeTransition kivy.uix.screenmanager.FadeTransition
