# Beginning-Python-Programs
Beginning Python Programs
# Exemplo de Uso de Tuplas em Python - Exercício 4-13: Buffet

Este repositório contém um exemplo simples de como utilizar **tuplas** em Python. O exercício 4-13 pede que criemos um menu de restaurante utilizando tuplas, imprimamos os itens com um `for` loop e mostremos a imutabilidade da tupla.

## Objetivos do Exercício
1. Criar uma **tupla** com cinco alimentos de um buffet.
2. Usar um **loop `for`** para imprimir cada item da tupla.
3. Tentar modificar um item da tupla (o que resultará em erro, pois tuplas são imutáveis).
4. Criar uma **nova tupla** com dois alimentos diferentes e imprimir o novo menu.

## Código Python

```python
# Criando a tupla com os cinco alimentos oferecidos pelo buffet
menu = ("Arroz", "Feijão", "Frango", "Salada", "Macarrão")

# Usando um loop for para imprimir cada alimento
print("Menu original:")
for item in menu:
    print(item)

# Tentando modificar um dos itens da tupla (Python deve rejeitar)
# menu[0] = "Batata"  # Isso resultaria em um erro, pois tuplas são imutáveis

# Alterando dois itens do menu (criando uma nova tupla)
menu = ("Arroz", "Feijão", "Peixe", "Legumes", "Macarrão")

# Imprimindo o novo menu
print("\nNovo menu:")
for item in menu:
    print(item)
```

## Explicação do Código
- Criamos uma **tupla** chamada `menu`, contendo cinco alimentos.
- Utilizamos um **loop `for`** para percorrer cada elemento da tupla e imprimi-lo na tela.
- Tentamos modificar um item da tupla, mas isso resulta em erro, pois **tuplas são imutáveis**.
- Para "modificar" o menu, **criamos uma nova tupla** com dois itens diferentes.
- Utilizamos novamente um `for` loop para imprimir o novo menu atualizado.

## Saída Esperada
Quando executamos o código, obtemos a seguinte saída:

```
Menu original:
Arroz
Feijão
Frango
Salada
Macarrão

Novo menu:
Arroz
Feijão
Peixe
Legumes
Macarrão
```

## Conceitos Importantes
- **Tuplas**: São semelhantes a listas, mas **são imutáveis**.
- **Loop `for in`**: Percorre cada elemento da tupla, um por um.
- **Criação de uma nova tupla**: Como não podemos modificar uma tupla diretamente, criamos uma nova tupla para substituir a anterior.

---

Este código é um excelente exemplo para entender a imutabilidade das tuplas e como utilizá-las eficientemente em Python. 🚀

