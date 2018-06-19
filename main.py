# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.core.window import Window
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
# from kivy.uix.button import Button
#
# class Home(Screen):
#     pass
#
# class Cadastro(Screen):
#     pass
#
# class Mesas(Screen):
#
#     def oi(self):
#         for i in range (0,35):
#             self.ids["outros"].add_widget(Button(text="oi"))
#
# class Login(Screen):
#     def login_valido(self):
#         #for l in self.logins:
#         if "a" == self.ids["ti_usuario"].text and "a" == self.ids["ti_senha"].text:
#             print ('login válido')
#             return True
#         self.ids["lb_primeiro"].text = "Login com erro"
#         print ('login inválido')
#         return False
#         #pass
#
# class ScreenManagement(ScreenManager):
#     def trocar_tela (self, tela):
#         self.current = tela
#         #pass
#
# class Tela(App):
#     def build(self):
#         return presentation
#
# presentation = Builder.load_file("tela.kv")
# Window.size = 500, 600 #Window.size = 500, 800  #original
#
# if __name__ == "__main__":
#     Tela().run()

#: import FadeTransition kivy.uix.screenmanager.FadeTransition

from conection.Conexao import Dados

Dados().novo()