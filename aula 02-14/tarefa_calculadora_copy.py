from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

from kivy.config import Config

from kivy.core.window import Window
import math

Window.size = (400, 700)

class MyCalc(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Exibição da operação com fundo branco e texto preto
        self.display = Label(
            text='0', 
            font_size="40", 
            size_hint=(1, 0.2),
            color=(0, 0, 0, 1)  # Cor do texto preta (RGBA)
        )
        
        # Adicionando um fundo branco ao Label usando canvas
        with self.display.canvas.before:
            Color(1, 1, 1, 1)  # Cor de fundo branca (RGBA)
            self.rect = Rectangle(size=self.display.size, pos=self.display.pos)

        # Atualiza o tamanho e a posição do fundo conforme o label
        self.display.bind(size=self.update_rect, pos=self.update_rect)

        # Layout para os botões
        caixa_botoes = GridLayout(cols=5)  # Alterado para 5 colunas

        # Definindo os botões
        self.botao1 = Button(text='1')
        self.botao2 = Button(text='2')
        self.botao3 = Button(text='3')
        self.botao4 = Button(text='4')
        self.botao5 = Button(text='5')
        self.botao6 = Button(text='6')
        self.botao7 = Button(text='7')
        self.botao8 = Button(text='8')
        self.botao9 = Button(text='9')
        self.botao0 = Button(text='0')
        self.botao_plus = Button(text='+')
        self.botao_minus = Button(text='-')
        self.botao_multiply = Button(text='*')
        self.botao_divide = Button(text='/')
        self.botao_equal = Button(text='=')
        self.botao_clear = Button(text='C')
        self.botao_del = Button(text='DEL')
        self.botao_pow = Button(text='^')
        self.botao_sqrt = Button(text='√')
        self.botao_percent = Button(text='%')  # Botão de porcentagem
        self.botao_comma = Button(text=',')  # Botão de vírgula

        # Definindo ações dos botões
        self.botao0.bind(on_press=self.armazenar)
        self.botao1.bind(on_press=self.armazenar)
        self.botao2.bind(on_press=self.armazenar)
        self.botao3.bind(on_press=self.armazenar)
        self.botao4.bind(on_press=self.armazenar)
        self.botao5.bind(on_press=self.armazenar)
        self.botao6.bind(on_press=self.armazenar)
        self.botao7.bind(on_press=self.armazenar)
        self.botao8.bind(on_press=self.armazenar)
        self.botao9.bind(on_press=self.armazenar)
        self.botao_plus.bind(on_press=self.armazenar)
        self.botao_minus.bind(on_press=self.armazenar)
        self.botao_multiply.bind(on_press=self.armazenar)
        self.botao_divide.bind(on_press=self.armazenar)
        self.botao_pow.bind(on_press=self.armazenar)
        self.botao_sqrt.bind(on_press=self.armazenar)
        self.botao_percent.bind(on_press=self.armazenar)  # Lógica para porcentagem
        self.botao_comma.bind(on_press=self.armazenar)  # Lógica para vírgula

        self.botao_equal.bind(on_press=self.calcular)
        self.botao_clear.bind(on_press=self.zerar)
        self.botao_del.bind(on_press=self.deletar)

        # Layout para os botões isolados (C e DEL)
        caixa_botoes_isolados = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        caixa_botoes_isolados.add_widget(self.botao_clear)
        caixa_botoes_isolados.add_widget(Widget())  # Espaço vazio entre C e DEL
        caixa_botoes_isolados.add_widget(self.botao_del)

        # Aumentando o tamanho dos botões C e DEL
        self.botao_clear.size_hint = (None, 1)
        self.botao_del.size_hint = (None, 1)
        self.botao_clear.width = 150  # Largura maior
        self.botao_del.width = 150  # Largura maior

        # Layout para os botões calculadora
        caixa_botoes.add_widget(self.botao7)
        caixa_botoes.add_widget(self.botao8)
        caixa_botoes.add_widget(self.botao9)
        caixa_botoes.add_widget(self.botao_divide)
        caixa_botoes.add_widget(self.botao_sqrt)

        caixa_botoes.add_widget(self.botao4)
        caixa_botoes.add_widget(self.botao5)
        caixa_botoes.add_widget(self.botao6)
        caixa_botoes.add_widget(self.botao_multiply)
        caixa_botoes.add_widget(self.botao_percent)

        caixa_botoes.add_widget(self.botao1)
        caixa_botoes.add_widget(self.botao2)
        caixa_botoes.add_widget(self.botao3)
        caixa_botoes.add_widget(self.botao_minus)
        caixa_botoes.add_widget(self.botao_pow)

        caixa_botoes.add_widget(self.botao0)
        caixa_botoes.add_widget(Button())  # Espaço em branco
        caixa_botoes.add_widget(self.botao_comma)
        caixa_botoes.add_widget(self.botao_plus)
        caixa_botoes.add_widget(self.botao_equal)

        # Adicionando a exibição e os layouts à interface
        layout.add_widget(self.display)
        layout.add_widget(caixa_botoes_isolados)  # Adicionando os botões C, espaço e DEL
        layout.add_widget(caixa_botoes)  # Layout com os botões de cálculo

        return layout

    def update_rect(self, *args):
        """Atualiza a posição e o tamanho do fundo"""
        self.rect.pos = self.display.pos
        self.rect.size = self.display.size

    def zerar(self, event):
        """Limpa a tela de exibição"""
        self.display.text = '0'

    def armazenar(self, event):
        """Armazena os números ou operadores pressionados"""
        if self.display.text == '0':
            self.display.text = event.text
        else:
            # Substituindo a vírgula por ponto para cálculos
            if event.text == ',':
                self.display.text += '.'
            else:
                self.display.text += event.text

    def calcular(self, event):
        """Realiza o cálculo da expressão"""
        try:
            # Substituindo a potenciação (^) por ** para Python
            expressao = self.display.text.replace('^', '**')

            # Realizando o cálculo com eval
            if '%' in expressao:
                expressao = expressao.replace('%', '/100')  # Converte o % para divisão por 100
                resultado = eval(expressao)
            else:
                resultado = eval(expressao)

            # Verificando se o resultado é uma raiz quadrada
            if '√' in self.display.text:
                self.display.text = str(math.sqrt(resultado))
            else:
                self.display.text = str(resultado)

        except Exception as e:
            self.display.text = 'Erro'

    def deletar(self, event):
        """Deleta o último número ou operador"""
        current_text = self.display.text
        if len(current_text) > 1:
            self.display.text = current_text[:-1]  # Remove o último caractere
        else:
            self.display.text = '0'  # Se só restar um caractere, volta para '0'

if __name__ == "__main__":
    MyCalc().run()
