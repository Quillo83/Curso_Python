class EvaluadorNumero:
    def __init__(self, num): 
        self.num = num

    def evaluarnum(self):
        if self.num & 1:
            print("Numerito impar")
        else:
            print("Numerito par")
            if self.num == 10:
                print("El numerito es 10")

        if self.num == 7:
            print("Tu numerito es comodín")

    def suma(self, numeritosuma):
        return self.num + numeritosuma


if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número: "))
        evaluador = EvaluadorNumero(numero)

        evaluador.evaluarnum()
        sumarealizada = evaluador.suma(2)
        print(f"Resultado de la suma con 2: {sumarealizada}")
    except ValueError:
        print("Por favor ingresa un número válido.")
        print("linea final.")
    
