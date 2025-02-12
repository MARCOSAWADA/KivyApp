# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.core.window import Window
# Window.size = (300,600)


# class Contador(App):
#     def build(self):
#         box_main = BoxLayout(orientation='vertical')

        # iniciamos a variável com self para poder alterar seu conteudo com as funções
#         input = Label(text="Bom dia", font_size="40")
#         botao = Button(text="continue clicando")

#         # quando clicar no botão chama a funçao contar
#         botao.bind(on_press = self.contar)

        # adicionando o input e o botao no layout
#         box_main.add_widget(input)
#         box_main.add_widget(botao)
        
#         return box_main
    
#     def contar(self,evento):
#         x = 1
#         print("contando...")
#         print(x)
    
# if __name__ == "__main__":
#     Contador().run()

# ____________________________________________________________

# class Contador(App):
#     def build(self):
#         box_main = BoxLayout(orientation='vertical')

#         self.input = Label(text="1", font_size="40")
#         botao = Button(text="continue clicando")

#         # quando clicar no botão chama a funçao contar
#         botao.bind(on_press = self.contar)

#         box_main.add_widget(self.input)
#         box_main.add_widget(botao)
        
#         return box_main
    
#     def contar(self,evento):
#         numero = self.input.text
#         print(numero)
#         # mostra se é inteiro ou string
#         print(type(numero))
    
# if __name__ == "__main__":
#     Contador().run()


# ____________________________________________________________


# class Contador(App):
#     def build(self):
#         box_main = BoxLayout(orientation='vertical')

#         self.input = Label(text="1", font_size="40")
#         botao = Button(text="continue clicando")

#         # quando clicar no botão chama a funçao contar
#         botao.bind(on_press = self.contar)

#         box_main.add_widget(self.input)
#         box_main.add_widget(botao)
        
#         return box_main
    
#     def contar(self,evento):
#         num = 1
#         num += int(self.input.text)
#         self.input.text = str(num)
#         print(num)
    
# if __name__ == "__main__":
#     Contador().run()


# ____________________________________________________________
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.core.window import Window
Window.size = (300,600)

class Contador(App):
    def build(self):
        box_main = BoxLayout(orientation='vertical')

        self.input = Label(text="1", font_size="40") 

        botao = Button(text="7")
        botao2 = Button(text="8")
        botao3 = Button(text="9")
        botao4 = Button(text="4")
        botao5 = Button(text="5")
        botao6 = Button(text="6")
        botao7 = Button(text="1")
        botao8 = Button(text="2")
        botao9 = Button(text="3")
        botao10 = Button(text="c")
        botao11 = Button(text="0")
        botao12 = Button(text=",")
        botao13 = Button(text="/")
        botao14 = Button(text="*")
        botao15 = Button(text="-")
        botao16 = Button(text="+")

        # quando clicar no botão chama a funçao contar
        botao.bind(on_press = self.contar)

        box_main.add_widget(self.input)
        box_main.add_widget(botao)
        box_main.add_widget(botao2)
        box_main.add_widget(botao3)
        box_main.add_widget(botao4)
        box_main.add_widget(botao5)
        box_main.add_widget(botao6)
        box_main.add_widget(botao7)
        box_main.add_widget(botao8)
        box_main.add_widget(botao9)
        box_main.add_widget(botao10)
        box_main.add_widget(botao11)
        box_main.add_widget(botao12)
        box_main.add_widget(botao13)
        box_main.add_widget(botao14)
        box_main.add_widget(botao15)
        box_main.add_widget(botao16)
        
        return box_main
    
    def contar(self,evento):
        num = 1
        num += int(self.input.text)
        self.input.text = str(num)
        print(num)
    
if __name__ == "__main__":
    Contador().run()




























# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout

# class Calculadora(App):
#     def build(self):
#         self.resultado = Label(text="0", font_size="40", halign="right", size_hint=(1, 0.2))
        
#         # Layout principal
#         layout = BoxLayout(orientation='vertical')
#         layout.add_widget(self.resultado)
        
#         # Layout para os botões
#         grid = GridLayout(cols=4)
        
#         # Definir os botões
#         botoes = [
#             ('7', self.adicionar_numero),
#             ('8', self.adicionar_numero),
#             ('9', self.adicionar_numero),
#             ('/', self.adicionar_operacao),
#             ('4', self.adicionar_numero),
#             ('5', self.adicionar_numero),
#             ('6', self.adicionar_numero),
#             ('*', self.adicionar_operacao),
#             ('1', self.adicionar_numero),
#             ('2', self.adicionar_numero),
#             ('3', self.adicionar_numero),
#             ('-', self.adicionar_operacao),
#             ('0', self.adicionar_numero),
#             ('.', self.adicionar_numero),
#             ('C', self.limpar),
#             ('+', self.adicionar_operacao),
#         ]
        
#         # Criar os botões e adicionar no grid
#         for (texto, acao) in botoes:
#             botao = Button(text=texto, on_press=acao)
#             grid.add_widget(botao)
        
#         # Botão para calcular o resultado
#         botao_resultado = Button(text="=", on_press=self.calcular)
#         layout.add_widget(grid)
#         layout.add_widget(botao_resultado)
        
#         return layout

#     def adicionar_numero(self, instance):
#         current_text = self.resultado.text
#         if current_text == "0":
#             self.resultado.text = instance.text
#         else:
#             self.resultado.text += instance.text
    
#     def adicionar_operacao(self, instance):
#         current_text = self.resultado.text
#         if current_text[-1] not in '+-*/':  # Não permitir adicionar operação se já houver uma
#             self.resultado.text += instance.text
    
#     def limpar(self, instance):
#         self.resultado.text = "0"
    
#     def calcular(self, instance):
#         try:
#             # Avaliar a expressão matemática que está no display
#             resultado = eval(self.resultado.text)
#             self.resultado.text = str(resultado)
#         except Exception as e:
#             self.resultado.text = "Erro"
        
# if __name__ == "__main__":
#     Calculadora().run()
