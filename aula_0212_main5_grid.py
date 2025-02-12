from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# DEFININDO O TAMANHO DA TELA DO APP
from kivy.core.window import Window
Window.size = (300,600)

# BOX LAYOUT é parecido com uma div

class MyCalc(App):
    def build(self):
        # variavel que contém uma CAIXA box para agrupar os elementos
        tela = BoxLayout(orientation = 'vertical')
        self.display = Label(text='Bem Vindo')

        self.lista = []

        layout = GridLayout(cols=2)

        self.botao1 = Button(text='1')
        self.botao2 = Button(text='2')
        self.botao3 = Button(text='+')
        self.botao4 = Button(text='=')

        # self.botao1.bind(on_press = self.mostrarvalor)

        self.botao1.bind(on_press = self.armazenar)
        self.botao2.bind(on_press = self.armazenar)
        self.botao3.bind(on_press = self.armazenar)
        self.botao4.bind(on_press = self.calcular)

        # Adicionando os WIDGETS na caixa
        layout.add_widget(self.botao1)
        layout.add_widget(self.botao2)
        layout.add_widget(self.botao3)
        layout.add_widget(self.botao4)

        tela.add_widget(self.display)
        tela.add_widget(layout)


        return tela
    
    # def mostrarvalor(self,event):
    #     # transforme uma string em inteiro
    #     num = int(self.botao1.text)
    #     print(type(num))

    # def calcular(self,event):
    #     # irá mostrar string
    #     num = self.botao4.text
    #     print(type(num))
    #     self.display.text = num

    def mostrarTela(self,lista):
        self.display.text = str(lista[0])

    def armazenar(self,event):
        self.lista.append( int(self.botao1.text) )
        self.mostrarTela(self.lista)

    def add(self,event):
        # self.botao1.text = ''
        number = int(self.botao1.text)
        self.display.text = ''
        self.display.text += str(number)
    
    def calcular(self,event):
        num = self.botao4.text
        print(type(num))
        self.display.text = num
    
if __name__ == "__main__":
    MyCalc().run()