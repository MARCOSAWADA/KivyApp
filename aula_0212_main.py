from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyCalc(App):
    def build(self):
        return Label(text="Hello")
    
if __name__ == "__main__":
    MyCalc().run()