# Exercício 7-1: Carro para Aluguel

Este é um exercício do **Capítulo 7** do livro *Python Crash Course, 3rd Edition*, onde o objetivo é solicitar ao usuário que informe um carro que deseja alugar e, em seguida, exibir uma mensagem personalizada com a resposta.

## 📌 Descrição do Problema
O programa deve:
1. Pedir ao usuário que informe o tipo de carro que gostaria de alugar.
2. Exibir uma mensagem confirmando que irá verificar a disponibilidade desse carro.

## 🛠 Tecnologias Utilizadas
- **Linguagem**: Python 3
- **Conceitos**: Entrada de dados (`input()`), Saída formatada (`print()` e `f-strings`), Manipulação de strings (`.title()`).

## 🚀 Como Executar o Programa
1. Certifique-se de ter o **Python** instalado em seu sistema.
2. Copie o seguinte código para um arquivo chamado `carro_aluguel.py`:

```python
# Solicita ao usuário que informe o tipo de carro que deseja alugar
carro_desejado = input("Que tipo de carro você gostaria de alugar? ")

# Exibe uma mensagem personalizada com o carro informado
print(f"Deixe-me ver se consigo um {carro_desejado.title()} para você.")
```

3. No terminal ou prompt de comando, navegue até o diretório onde salvou o arquivo e execute:
   ```sh
   python carro_aluguel.py
   ```
4. Digite o nome de um carro quando solicitado e veja a resposta do programa.

## 🎯 Exemplo de Execução
```
Que tipo de carro você gostaria de alugar? ferrari
Deixe-me ver se consigo um Ferrari para você.
```

## 📖 Aprendizados
Este exercício reforça:
- Como capturar e manipular a entrada do usuário.
- O uso de `print()` para exibir mensagens formatadas.
- O uso de `.title()` para melhorar a formatação do texto.

## 📌 Referências
- *Python Crash Course, 3rd Edition* - Eric Matthes
- [Documentação Oficial do Python](https://docs.python.org/3/)

---
Se tiver dúvidas ou quiser melhorias no código, sinta-se à vontade para sugerir! 🚀

