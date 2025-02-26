# Desenho de um Carro com Turtle em Python

Este repositório contém um programa em Python que desenha um carro utilizando a biblioteca **Turtle**.

## 📌 Descrição do Programa
O programa utiliza a biblioteca `turtle` para desenhar um carro simples. O desenho é composto pelos seguintes elementos:
- **Corpo do carro**: Um retângulo verde representando a parte principal do carro.
- **Janelas e teto**: Linhas inclinadas formam o teto e a divisão das janelas.
- **Rodas**: Duas rodas pretas desenhadas com círculos.

## 🛠 Tecnologias Utilizadas
- **Linguagem**: Python 3
- **Bibliotecas**: `turtle`

## 🚀 Como Executar o Programa

1. **Pré-requisitos**:
   - Certifique-se de ter o **Python 3** instalado.
   - Nenhuma biblioteca adicional precisa ser instalada, pois `turtle` já vem com o Python.

2. **Código-fonte**:
   - Copie o seguinte código para um arquivo chamado `desenho_carro.py`:

```python
# Importação da biblioteca
import turtle

car = turtle.Turtle()

# Desenhando o corpo do carro
car.color('#008000')
car.fillcolor('#008000')
car.penup()
car.goto(0,0)
car.pendown()
car.begin_fill()
car.forward(370)
car.left(90)
car.forward(50)
car.left(90)
car.forward(370)
car.left(90)
car.forward(50)
car.end_fill()

# Desenhando o teto e as janelas
car.penup()
car.goto(100, 50)
car.pendown()
car.setheading(45)
car.forward(70)
car.setheading(0)
car.forward(100)
car.setheading(-45)
car.forward(70)
car.setheading(90)
car.penup()
car.goto(200, 50)
car.pendown()
car.forward(49.50)

# Desenhando as rodas
car.penup()
car.goto(100, -10)
car.pendown()
car.color('#000000')
car.fillcolor('#000000')
car.begin_fill()
car.circle(20)
car.end_fill()
car.penup()
car.goto(300, -10)
car.pendown()
car.color('#000000')
car.fillcolor('#000000')
car.begin_fill()
car.circle(20)
car.end_fill()

car.hideturtle()

turtle.done()
```

3. **Execução:**
   - Abra o terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo `desenho_carro.py` está salvo.
   - Execute o script com o comando:

     ```sh
     python desenho_carro.py
     ```

4. **Resultado Esperado:**
   - Um carro verde com duas rodas pretas será desenhado na tela usando a biblioteca Turtle.

## 🎯 Aprendizados

Este programa reforça os seguintes conceitos:
- Uso da biblioteca `turtle` para desenho gráfico em Python.
- Manipulação de posição e direção de um objeto `Turtle`.
- Desenho de formas geométricas básicas como retângulos e círculos.

## 📌 Referências
- Documentação Oficial do Turtle: [docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)
https://www.geeksforgeeks.org/draw-a-car-using-turtle-in-python/

---
Se tiver dúvidas ou sugestões, sinta-se à vontade para compartilhar! 🚀

