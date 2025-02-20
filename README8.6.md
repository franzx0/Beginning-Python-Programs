# Exercício 8-6: Nomes de Cidades

Este repositório contém a solução para o **Exercício 8-6** do livro *Python Crash Course, 3ª Edição*. O objetivo é criar uma função que receba o nome de uma cidade e seu país, retornando uma string formatada.

## 📌 Descrição do Problema
O programa deve:
1. Criar uma função chamada `city_country()` que aceite o nome de uma cidade e seu país.
2. Retornar uma string formatada como "Santiago, Chile".
3. Chamar a função com pelo menos **três pares cidade-país** e imprimir os valores retornados.

## 🛠 Tecnologias Utilizadas
- **Linguagem**: Python 3
- **Conceitos**: Definição de funções, passagem de argumentos, formatação de strings.

## 🚀 Como Executar o Programa

1. **Pré-requisitos**: Certifique-se de ter o Python 3 instalado em seu sistema.

2. **Código-fonte**: Copie o seguinte código para um arquivo chamado `city_country.py`:

```python
def city_country(cidade, pais):
    """Retorna uma string no formato 'Cidade, País'."""
    return f"{cidade.title()}, {pais.title()}"

# Chamadas da função com diferentes pares cidade-país
print(city_country('santiago', 'chile'))
print(city_country('rio de janeiro', 'brasil'))
print(city_country('nova york', 'estados unidos'))
```

3. **Execução:**
   - Abra o terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo `city_country.py` está salvo.
   - Execute o script com o comando:

     ```sh
     python city_country.py
     ```

4. **Resultado Esperado:**
   ```
   Santiago, Chile
   Rio De Janeiro, Brasil
   Nova York, Estados Unidos
   ```

## 🎯 Aprendizados

Este exercício reforça os seguintes conceitos:

- **Definição de Funções**: Como criar funções que recebem parâmetros e retornam valores.
- **Formatação de Strings**: Uso do método `.title()` para capitalizar palavras e f-strings para interpolar valores.
- **Passagem de Argumentos**: Como passar argumentos posicionais para funções em Python.

## 📌 Referências
- *Python Crash Course, 3ª Edição* - Eric Matthes
- [Documentação Oficial do Python](https://docs.python.org/3/)

---
Se tiver dúvidas ou sugestões, sinta-se à vontade para compartilhar! 🚀

