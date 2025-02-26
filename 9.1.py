class Restaurante:
    """Uma classe que representa um restaurante."""

    def __init__(self, nome_restaurante, tipo_cozinha):
        """Inicializa os atributos nome_restaurante e tipo_cozinha."""
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

    def descrever_restaurante(self):
        """Exibe uma descrição do restaurante."""
        print(f"O restaurante {self.nome_restaurante} serve comida {self.tipo_cozinha}.")

    def abrir_restaurante(self):
        """Exibe uma mensagem informando que o restaurante está aberto."""
        print(f"O restaurante {self.nome_restaurante} está agora aberto!")

# Criando uma instância da classe Restaurante
meu_restaurante = Restaurante('Sabor Brasileiro', 'brasileira')

# Exibindo os atributos individualmente
print(meu_restaurante.nome_restaurante)
print(meu_restaurante.tipo_cozinha)

# Chamando os métodos da instância
meu_restaurante.descrever_restaurante()
meu_restaurante.abrir_restaurante()
