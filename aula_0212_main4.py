from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# DEFININDO O TAMANHO DA TELA DO APP
from kivy.core.window import Window
Window.size = (300,600)

# BOX LAYOUT é parecido com uma div

class MyCalc(App):
    def build(self):
        # variavel que contém uma CAIXA box para agrupar os elementos
        layout = BoxLayout(orientation='vertical')

        tela = TextInput()

        texto1 = Label(text='Mycalc', font_size='20sp')
        botao = Button(text='Clique', font_size='20sp')

        # Adicionando os WIDGETS na caixa
        layout.add_widget(tela)
        layout.add_widget(texto1)
        layout.add_widget(botao)

        return layout
    
if __name__ == "__main__":
    MyCalc().run()