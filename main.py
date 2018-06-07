from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class Home(Screen):
    pass


class Cadastro(Screen):
    pass


class Login(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class Tela(App):
    def build(self):
        return presentation


presentation = Builder.load_file("tela.kv")
Window.size = 500, 800

if __name__ == "__main__":
    Tela().run()
