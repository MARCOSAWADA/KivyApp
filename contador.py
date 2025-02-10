from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size = (300,600)

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
