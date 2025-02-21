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

        # Exibindo a operação com fundo branco e texto preto
        self.display = Label(
            text='0', 
            font_size="80", 
            size_hint=(1, 0.2),
            color=(0, 0, 0, 1)
        )
        
        # Adicionando um fundo branco ao Label usando canvas
        with self.display.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.display.size, pos=self.display.pos)

        # Atualizando o tamanho e a posição do fundo conforme o label
        self.display.bind(size=self.update_rect, pos=self.update_rect)

        caixa_botoes = GridLayout(cols=5)

        self.botao1 = Button(text='1' , color = (0, 0, 100) ,font_size = "40")
        self.botao2 = Button(text='2' , color = (0, 0, 100) ,font_size = "40")
        self.botao3 = Button(text='3' , color = (0, 0, 100) ,font_size = "40")
        self.botao4 = Button(text='4' , color = (0, 0, 100) ,font_size = "40")
        self.botao5 = Button(text='5' , color = (0, 0, 100) ,font_size = "40")
        self.botao6 = Button(text='6' , color = (0, 0, 100) ,font_size = "40")
        self.botao7 = Button(text='7' , color = (0, 0, 100) ,font_size = "40")
        self.botao8 = Button(text='8' , color = (0, 0, 100) ,font_size = "40")
        self.botao9 = Button(text='9' , color = (0, 0, 100) ,font_size = "40")
        self.botao0 = Button(text='0' , color = (0, 0, 100) ,font_size = "40")
        self.botao_adição = Button(text='+' , color = (100, 0, 0) ,font_size = "50")
        self.botao_subtração = Button(text='-' , color = (100, 0, 0) ,font_size = "50")
        self.botao_multiplicação = Button(text='*' , color = (100, 0, 0) ,font_size = "50")
        self.botao_divisão = Button(text='/' , color = (100, 0, 0) ,font_size = "50")
        self.botao_igual = Button(text='=' , color = (100, 100, 100) ,font_size = "50")
        self.botao_limpar = Button(text='C' , color = (100, 0, 0) ,font_size = "50")
        self.botao_deletar = Button(text='<-' , color = (100, 100, 100) ,font_size = "50")
        self.botao_potenciação = Button(text='x²' , color = (0, 0, 100) ,font_size = "50")
        self.botao_raiz = Button(text='√' , color = (0, 0, 100) ,font_size = "50")
        self.botao_porcentagem = Button(text='%' , color = (0, 0, 100) ,font_size = "50")
        self.botao_virgula = Button(text='.' , color = (0, 0, 100) ,font_size = "40")  # Botão de vírgula


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
        self.botao_adição.bind(on_press=self.armazenar)
        self.botao_subtração.bind(on_press=self.armazenar)
        self.botao_multiplicação.bind(on_press=self.armazenar)
        self.botao_divisão.bind(on_press=self.armazenar)
        self.botao_potenciação.bind(on_press=self.armazenar)
        self.botao_raiz.bind(on_press=self.armazenar)
        self.botao_porcentagem.bind(on_press=self.armazenar)  # Lógica para porcentagem
        self.botao_virgula.bind(on_press=self.armazenar)  # Lógica para vírgula

        self.botao_igual.bind(on_press=self.calcular)
        self.botao_limpar.bind(on_press=self.zerar)
        self.botao_deletar.bind(on_press=self.deletar)

        # Layout para os botões isolados (Limpar e Deletar)
        caixa_botoes_isolados = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        caixa_botoes_isolados.add_widget(self.botao_limpar)
        caixa_botoes_isolados.add_widget(Widget())  # Espaço vazio entre Limpar e Deletar
        caixa_botoes_isolados.add_widget(self.botao_deletar)

        # Auterações do tamanho dos botões Limpar e Deletar
        self.botao_limpar.size_hint = (None, 1)
        self.botao_deletar.size_hint = (None, 1)
        self.botao_limpar.width = 250
        self.botao_deletar.width = 250 

        # Layout
        caixa_botoes.add_widget(self.botao7)
        caixa_botoes.add_widget(self.botao8)
        caixa_botoes.add_widget(self.botao9)
        caixa_botoes.add_widget(self.botao_divisão)
        caixa_botoes.add_widget(self.botao_raiz)

        caixa_botoes.add_widget(self.botao4)
        caixa_botoes.add_widget(self.botao5)
        caixa_botoes.add_widget(self.botao6)
        caixa_botoes.add_widget(self.botao_multiplicação)
        caixa_botoes.add_widget(self.botao_porcentagem)

        caixa_botoes.add_widget(self.botao1)
        caixa_botoes.add_widget(self.botao2)
        caixa_botoes.add_widget(self.botao3)
        caixa_botoes.add_widget(self.botao_subtração)
        caixa_botoes.add_widget(self.botao_potenciação)

        caixa_botoes.add_widget(self.botao0)
        caixa_botoes.add_widget(self.botao_virgula)
        caixa_botoes.add_widget(Widget())  # Espaço em branco
        caixa_botoes.add_widget(self.botao_adição)
        caixa_botoes.add_widget(self.botao_igual)

        # Adicionando a exibição e os layouts à interface
        layout.add_widget(self.display)
        layout.add_widget(caixa_botoes_isolados)  #botões Limpar, espaço e Deletar
        layout.add_widget(caixa_botoes)  # botões de cálculo

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
            if event.text == 'Vírgula':
                self.display.text += '.'
            else:
                self.display.text += event.text

    def calcular(self, event):
        """Realiza o cálculo da expressão"""
        try:
            expressao = self.display.text

            # Substituir o operador de potência por '**' (potenciação)
            expressao = expressao.replace('x²', '**2')

            # Tratar a porcentagem, convertendo para uma divisão por 100
            if '%' in expressao:
                expressao = expressao.replace('%', '/100')

            # Verificando e tratando a raiz quadrada antes do cálculo
            if '√' in expressao:
                expressao = expressao.replace('√', '')  # Remover o símbolo da raiz
                resultado = math.sqrt(float(expressao))  # Calcula a raiz quadrada diretamente
                self.display.text = str(resultado)
                return  # Não precisamos continuar após calcular a raiz quadrada

            # Realizando o cálculo com eval, agora mais seguro após os ajustes
            resultado = eval(expressao)

            self.display.text = str(resultado)

        except Exception as e:
            self.display.text = 'Erro'

    def deletar(self, event):
        """Deleta o último número ou operador"""
        current_text = self.display.text
        if len(current_text) > 1:
            self.display.text = current_text[:-1]
        else:
            self.display.text = '0'  # Se só restar um caractere, volta para '0'

if __name__ == "__main__":
    MyCalc().run()
