from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# BOX LAYOUT é parecido com uma div

class MyCalc(App):
    def build(self):
        # variavel que contém uma CAIXA box para agrupar os elementos
        layout = BoxLayout(orientation='vertical')

        texto1 = Label(text='Mycalc')
        botao = Button(text='Clique')

        # Adicionando os WIDGETS na caixa
        layout.add_widget(texto1)
        layout.add_widget(botao)

        return layout
    
if __name__ == "__main__":
    MyCalc().run()