# Exercício de Dicionário de Cidades

Este projeto é uma solução para o **Exercício 6-11** do Capítulo 6 do livro **"Python Crash Course, 3ª Edição"**. O exercício demonstra o uso de dicionários, incluindo dicionários aninhados, em Python.

---

## Descrição

O objetivo do exercício é:
1. Criar um dicionário chamado `cities` onde:
   - As chaves são os nomes de três cidades.
   - Cada cidade contém outro dicionário com informações sobre a cidade, incluindo:
     - O país em que a cidade está localizada.
     - A população aproximada da cidade.
     - Um fato sobre a cidade.
2. Utilizar um laço para exibir o nome de cada cidade e as informações associadas de forma clara.

---

## Conceitos Utilizados

Este exercício aplica os conceitos aprendidos no Capítulo 6 do livro:
- **Dicionários**: Uma coleção de pares chave-valor.
- **Dicionários Aninhados**: Dicionários dentro de dicionários para armazenar informações mais complexas.
- **Laços de Repetição**: Iteração sobre os itens de um dicionário usando `for`.
- **Acesso aos Valores**: Utilizando as chaves para acessar valores nos dicionários.

---

## Exemplo de Código

Aqui está o código Python usado para resolver o problema:

```python
# Criando o dicionário cities
cities = {
    "Tokyo": {
        "country": "Japão",
        "population": "14 milhões",
        "fact": "Tóquio é a maior área metropolitana do mundo."
    },
    "New York": {
        "country": "EUA",
        "population": "8,8 milhões",
        "fact": "Nova York é conhecida como a 'Big Apple'."
    },
    "Paris": {
        "country": "França",
        "population": "2,2 milhões",
        "fact": "Paris é famosa por abrigar a icônica Torre Eiffel."
    }
}

# Exibindo as informações de cada cidade
for city, details in cities.items():
    print(f"\nCidade: {city}")
    print(f"País: {details['country']}")
    print(f"População: {details['population']}")
    print(f"Fato: {details['fact']}")
