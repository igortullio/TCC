from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button, Label
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner


class Home(Screen):
    pass


class Cadastro(Screen):

    def realizar_cadastro(self):
        Dados().novo(self.ids["ti_usuario"].text, self.ids["ti_senha"].text,
                     self.ids["ti_email"].text)  # método para cadastrar
        self.ids["lb_cadastro1"].text = "Cadastro realizado com sucesso"


class Mesas(Screen):

    def oi(self):
        j = 1
        for i in range(0, 25):
            if i % 2 == 0:
                if j < 4:
                    self.ids["outros"].add_widget(Label(text=""))
                    j += 1
                else:
                    self.ids["outros"].add_widget(Label(text="Mesa"))
                    if j == 5:
                        j = 1
                    else:
                        j += 1
            else:
                self.ids["outros"].add_widget(Button(background_color=(0, 128, 0, 0.7), text="Cadeira"))

    def incrementa(self):
        global j
        if j == 5:
            j = 5
        else:
            j += 1


class Login(Screen):

    def login_valido(self):
        if Dados().login(self.ids["ti_usuario"].text,
                         self.ids["ti_senha"].text):  # chamada método verificar login no banco
            return True


class Esqueci(Screen):
    pass


class Opcao(Screen):
    pass


class Confirmacao(Screen):
    pass


class ScreenManagement(ScreenManager):

    def trocar_tela(self, tela):
        self.current = tela


class Tela(App):

    def build(self):
        return presentation


presentation = Builder.load_file("tela.kv")
Window.size = 500, 600  # Window.size = 500, 800  #original

if __name__ == "__main__":
    from conection.Conexao import Dados

    Dados().getCon()  # criar banco
    Tela().run()
