from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window
Window.size = (400,700)

class MyCalc(App):
    def build(self):

        layout = BoxLayout(orientation='vertical')

# --------------------------------------------------------

        self.botao0 = Button(text='ZeRaR')
        self.botao0.size_hint = (1.0, 0.3)

        self.display = Label(text='WeLcOmE' ,font_size = "40")

        caixa_botoes = GridLayout(cols=2)

        self.botao1 = Button(text='1')
        self.botao2 = Button(text='2')
        self.botao3 = Button(text='+')
        self.botao4 = Button(text='=')

    # bind é uma função que ao clicar nesse botão chama um método da classe
        self.botao0.bind(on_press = self.zerar)
        self.botao1.bind(on_press = self.armazenar)
        self.botao2.bind(on_press = self.armazenar)
        self.botao3.bind(on_press = self.armazenar)
        self.botao4.bind(on_press = self.calcular)

        caixa_botoes.add_widget(self.botao1)
        caixa_botoes.add_widget(self.botao2)
        caixa_botoes.add_widget(self.botao3)
        caixa_botoes.add_widget(self.botao4)

# ________________________________________________________
# chama a variável para mostrar no layout

        layout.add_widget(self.botao0) 
        layout.add_widget(self.display)
        layout.add_widget(caixa_botoes)

        return layout
    
    def zerar(self,event):
        self.display.text = ''

    def armazenar(self,event):
        self.display.text += event.text

    def calcular(self,event):
        # print(self.display.text)
        # # print(type(self.display.text))
    # __________________________________________
        # numbers = self.display.text.split("+")
        # print(numbers)
    # __________________________________________

        if "+" in self.display.text:
            numbers = self.display.text.split("+")
            # print(numbers)
            soma = int(numbers[0]) * int(numbers[1])
            # 
            self.display.text = str(soma)
    
if __name__ == "__main__":
    MyCalc().run()