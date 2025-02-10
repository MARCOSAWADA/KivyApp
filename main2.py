from kivy.app import App
from kivy.uix.button import Button

class SecondApp(App):
    def build(self):
        return Button(text='CLIQUE')
    
SecondApp().run()