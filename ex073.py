#73

class Calculadora:

    def soma(self, n1,n2):
        return n1+n2

    def sub(self, n1,n2):
        return n1-n2

    def mult(self, n1,n2):
        return n1*n2

    def div(self, n1,n2):
        return n1/n2

n1 = Calculadora()

print(n1.soma(1,6))