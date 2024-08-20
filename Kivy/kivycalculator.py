from kivy.config import Config
Config.set('kivy', 'keyborad_mode', 'systemanddock')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators= ["/", "*", "+", "-"]                    # Nas linhas de 8 a 10, criamos uma lista de operators e alguns valores úteis, last_was_operatore last_button, que nós usaremos mais tarde.
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation='vertical')             # Nas linhas de 11 a 15, criamos um layoutmain_layout de nível superior e adicionamosum widget TextInput somente leitura a ele
        self.solution = TextInput(multiline = False, readonly = True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)

        buttons = [                                 
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],                           # Nas linhas de 16 a 21, nós criamos uma listaaninhada de listas contendo a maioria dosnossos buttons para a calculadora
            ["3", "2", "1", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:                                # Na linha 22, nós iniciamos um forloop sobre aqueles buttons.Para cada listaaninhada, fizemos o seguinte
            h_layout = BoxLayout()                         # Na linha 23, criamos um BoxLayout com orientação horizontal;
            for label in row:                              # Na linha 24, iniciamos outro loop sobre os itens da lista aninhada; 
                button = Button(                           # Nas linhas de 25 a 39, nós criamos os botõespara a linha, os vinculamos a um manipuladorde eventos e adicionamos os botões à horizontalBoxLayout da linha 23
                    text = label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                button.bind(on_press= self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)                # Na linha 31, você adiciona esse layout ao arquivomain_layout
        
        equals_button = Button(                             # Nas linhas de 33 a 37, você cria o botão igual (=),associa-o a um manipulador de eventos e adiciona-oa main_layout.
            text='=', pos_hint={'center_x':0.5 , 'center_y':0.5 }
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout
    
# proxima etapa é criar o manipulador de eventos on_button_press()

    def on_button_press(self, instance):                    # Na linha 43 recebe o argumento instance para que voce possa acessar qual widget chamou a função
        current = self.solution.text                        # Linha 44 e 45 extraem e armazenam o valor do solution e do botão text.
        button_text = instance.text
        
        if button_text == 'C':                              # As linhas de 45 a 47 verificam qual botão foi pressionado. Se ousuário pressionou C, você limpará o arquivo solution. Caso contrário,vá para a declaração else.
            # Clear the solution widget
            self.solution.text = ''
        else:
            if current and (                                # Verifica se a solução possuialgum valor pré-existente.
                self.last_was_operator and button_text in self.operators):          # verificam se o último botãopressionado foi um botão do operador. Se foi, entãosolution não será atualizado. 
                # Dont add two operators right after each other                    # Isso é para evitar queo usuário tenha dois operadores seguidos.Por exemplo, 1 */ não é uma declaração válida.
                return
            elif current == '' and button_text in self.operators:
                # First character cannot be an operator   
                return
            else:
                new_text= current + button_text                                     # Se nenhuma dascondições anteriores for atendida, atualize o solution
                self.solution.text = new_text
            self.last_button = button_text                                          # Define last_button no rótulo do último botão pressionado.
            self.last_was_operator = self.last_button in self.operators             # É definida last_was_operatorcomo True ou False dependendo se eraou não um caractere de operador

# Ultima parte do código a ser digitada e o on_solution() 

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

# Mais uma vez, pega o texto atual solution e usa o built-in eval() do Python para executá-lo.  
            
if __name__ == '__main__':
    app = MainApp()
    app.run()