from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MeuAplicativo(App):
    def build(self):
        box_main = BoxLayout(orientation='vertical', padding=[20], spacing=50)

        box_reader = BoxLayout()
        box_footer = BoxLayout(orientation="horizontal", padding=[0], spacing=50)

        box1 = BoxLayout()
        botao1 = TextInput(text='1')
        box1.add_widget(botao1)

        box2 = BoxLayout()
        botao2 = TextInput(text='2')
        box2.add_widget(botao2)

        box3 = BoxLayout()
        botao3 = TextInput(text='3')
        box3.add_widget(botao3)

        box4 = BoxLayout()
        botao4 = TextInput(text='4')
        box4.add_widget(botao4)

        box_reader.add_widget(box1)
        box_reader.add_widget(box2)

        box_footer.add_widget(box3)
        box_footer.add_widget(box4)

        box_main.add_widget(box_reader)
        box_main.add_widget(box_footer)

        return box_main
    
MeuAplicativo().run()