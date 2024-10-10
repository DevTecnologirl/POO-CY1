class Carro: #ABSTRACAO 
    def __init__(self, modelo, cor, velocidade_max):
        self.modelo = modelo
        self.cor = cor
        self.velocidade_max = velocidade_max 
        self.__combustivel = 100 #combustivel é encapsulado
    
    def ligar(self):
        print("CARRO LIGADO! VRUMMMMMMM VRUMMMMMM")
    
    #ENCAPSULAMENTO
    def abastecer(self, quantidade):
        self.__combustivel += quantidade
        print(f"Abastecido com {quantidade} litros!")

    def verificar_combustivel(self):
        return self.__combustivel

    #HERANCA
class CarroEsportivo(Carro):
    def __init__(self, modelo, cor):
        super().__init__(modelo, cor, 300)  # Velocidade maxima definida para esportivos
    
    def acelerar(self, incremento):
        super().acelerar(incremento * 1.5)  # Aceleracao maior para esportivos
    
    def dirigir(self):
        print(f"Dirigindo o carro {self.modelo}")

class CarroSUV(Carro):
    def __init__(self, modelo, cor):
        super().__init__(modelo, cor, 200)  # Velocidade maxima definida para SUVs
    def acelerar(self, incremento):
        super().acelerar(incremento * 1.2)  # Aceleracao ligeiramente maior para SUVs
    def dirigir(self):
        print(f"Dirigindo o carro SUV {self.modelo} em um terreno acidentado!")

# Usando os carros
carro1 = CarroEsportivo("Ferrari")
carro2 = CarroSUV("Toyota RAV4")

carro1.dirigir()  # Saída: Dirigindo o carro esportivo Ferrari a toda velocidade!
carro2.dirigir()  # Saída: Dirigindo o carro SUV Toyota RAV4 em um terreno acidentado!