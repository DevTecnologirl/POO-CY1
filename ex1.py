class Carro:
    def __init__(self, marca, modelo, ano, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = combustivel
        self.velocidade = 0 #Todo carro inicia com velocidade 0 Km/h

    def ligar(self):
        print("O carro esta ligado! VRUMMMMM VRUMMMMMM")
    
    def desligar(self):
        print("O carro esta desligado!")

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"Acelerando... Velocidade atual: {self.velocidade} km/h.")
    
    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Freiando... Velocidade atual: {self.velocidade} km/h.")
    
    # Getter para a velocidade
    def get_velocidade(self):
        return self.velocidade

    # Setter para a velocidade
    def set_velocidade(self, nova_velocidade):
        if nova_velocidade >= 0:
            self.velocidade = nova_velocidade
        else:
            print("Velocidade não pode ser negativa.")
    
meuCarro = Carro("Toyota", "Corolla", 2020, "vermelho", "gasolina")
meuCarro.exibir_info()
meuCarro.ligar()
meuCarro.acelerar(60)
meuCarro.mover()
meuCarro.frear(30)
print(f"A velocidade atual é: {meuCarro.get_velocidade()} km/h")  # Usando o getter
meuCarro.set_velocidade(-10)   # Testando o setter com valor negativo
