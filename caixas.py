from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuAplicativo(App):
    def build(self):
        box_main = BoxLayout(orientation='vertical')

        box_reader = BoxLayout()
        box_footer = BoxLayout(orientation="horizontal")

        box1 = BoxLayout()
        texto1 = Label(text='1')
        box1.add_widget(texto1)

        box2 = BoxLayout()
        texto2 = Label(text='2')
        box2.add_widget(texto2)

        box3 = BoxLayout()
        texto3 = Label(text='3')
        box3.add_widget(texto3)

        box4 = BoxLayout()
        texto4 = Label(text='4')
        box4.add_widget(texto4)

        box_reader.add_widget(box1)
        box_reader.add_widget(box2)

        box_footer.add_widget(box3)
        box_footer.add_widget(box4)

        box_main.add_widget(box_reader)
        box_main.add_widget(box_footer)

        return box_main
    
MeuAplicativo().run()