class Carro:
    def __init__(self, marca, modelo, ano):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo protegido
        self._ano = ano  # Atributo protegido

    # Método getter para a marca
    def get_marca(self):
        return self._marca

    # Método setter para a marca
    def set_marca(self, marca):
        self._marca = marca

    # Método getter para o modelo
    def get_modelo(self):
        return self._modelo

    # Método setter para o modelo
    def set_modelo(self, modelo):
        self._modelo = modelo

    # Método getter para o ano
    def get_ano(self):
        return self._ano

    # Método setter para o ano
    def set_ano(self, ano):
        if ano > 1885:  # O primeiro carro foi inventado em 1886
            self._ano = ano
        else:
            print("Ano inválido. O ano deve ser maior que 1885.")

    def __str__(self):
        return f"{self._marca} {self._modelo} - {self._ano}"


# Exemplo de uso da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)

# Usando getters
print(carro1.get_marca())  # Toyota
print(carro1.get_modelo())  # Corolla
print(carro1.get_ano())  # 2020

# Usando setters
carro1.set_marca("Honda")
carro1.set_modelo("Civic")
carro1.set_ano(2022)

# Verificando as mudanças
print(carro1)  # Honda Civic - 2022

# Tentando definir um ano inválido
carro1.set_ano(1800)  # Ano inválido. O ano deve ser maior que 1885.
print(carro1)  # Honda Civic - 2022
