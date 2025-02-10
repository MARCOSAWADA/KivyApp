from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuAplicativo(App):
    def build(self):
        box = BoxLayout(orientation='horizontal')
        label = Label(text='Meu App')
        botao = Button(text="Clique aqui")
        box.add_widget(label)
        box.add_widget(botao)
        return box
    
MeuAplicativo().run()