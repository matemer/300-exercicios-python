'''96 – Crie uma estrutura toda orientada a objetos que recebe do usuário uma string qualquer, retornando a mesma com todas suas letras 
convertidas para letra maiúscula. Os métodos de classe para cada funcionalidade devem ser independentes entre si, porém trabalhar no escopo geral da classe.'''

class Letra:
    def __init(self):
        self.s = ""

    def recebe_string(self):
        self.s = input("Digite uma palavra/frase: ")

    def exibe_string(self):
        print(self.s.upper())

frase1 = Letra()

frase1.recebe_string()
frase1.exibe_string()