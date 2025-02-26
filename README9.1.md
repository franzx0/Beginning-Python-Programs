# Exercício 9-1: Restaurante

Este repositório contém a solução para o **Exercício 9-1** do livro *Python Crash Course, 3ª Edição*. O objetivo é criar uma classe que represente um restaurante e implemente métodos para descrever e abrir o restaurante.

## 📌 Descrição do Problema
O programa deve:
1. Criar uma classe chamada `Restaurante` com dois atributos: `nome_restaurante` e `tipo_cozinha`.
2. Criar um método chamado `descrever_restaurante()` que exiba uma mensagem descrevendo o restaurante.
3. Criar um método chamado `abrir_restaurante()` que exiba uma mensagem informando que o restaurante está aberto.
4. Criar uma instância da classe e chamar os métodos para testar a funcionalidade.

## 🛠 Tecnologias Utilizadas
- **Linguagem**: Python 3
- **Conceitos**: Classes, Objetos, Métodos, Instanciação

## 🚀 Como Executar o Programa

1. **Pré-requisitos**: Certifique-se de ter o Python 3 instalado em seu sistema.

2. **Código-fonte**: Copie o seguinte código para um arquivo chamado `restaurante.py`:

```python
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
```

3. **Execução:**
   - Abra o terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo `restaurante.py` está salvo.
   - Execute o script com o comando:

     ```sh
     python restaurante.py
     ```

4. **Resultado Esperado:**
   ```
   Sabor Brasileiro
   brasileira
   O restaurante Sabor Brasileiro serve comida brasileira.
   O restaurante Sabor Brasileiro está agora aberto!
   ```

## 🎯 Aprendizados

Este exercício reforça os seguintes conceitos:

- **Criação de Classes:** Como definir uma classe e seus atributos.
- **Definição de Métodos:** Como criar funções dentro de uma classe para realizar ações específicas.
- **Instanciação de Objetos:** Como criar e utilizar objetos de uma classe.
- **Uso de `__init__()`** para inicializar atributos automaticamente.

## 📌 Referências
- *Python Crash Course, 3ª Edição* - Eric Matthes
- [Documentação Oficial do Python](https://docs.python.org/3/)

---
Se tiver dúvidas ou sugestões, sinta-se à vontade para compartilhar! 🚀
