from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuAplicativo(App):
    def build(self):
        box = BoxLayout(orientation='vertical', padding=[10], spacing=10)

        box1 = BoxLayout(orientation='horizontal')
        box2 = BoxLayout(orientation='vertical')

        botao1 = Button(text="Clique 1")
        botao2 = Button(text="Clique 2")
        botao3 = Button(text="Clique 3")
        botao4 = Button(text="Clique 4")


        box.add_widget(box1)
        box.add_widget(box2)

        box1.add_widget(botao1)
        box1.add_widget(botao2)
        box2.add_widget(botao3)
        box2.add_widget(botao4)
        return box

MeuAplicativo().run()