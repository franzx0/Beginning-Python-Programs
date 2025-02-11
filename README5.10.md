# Verificando Nomes de Usuários

Este projeto é a solução para o **Exercício 5-10** do Capítulo 5 do livro **"Python Crash Course, 3ª Edição"**. O objetivo do exercício é simular como os sites garantem que todos os usuários tenham um nome de usuário único.

---

## Descrição do Exercício

O programa realiza as seguintes tarefas:
1. Cria uma lista com cinco ou mais nomes de usuários já existentes, chamada `current_users`.
2. Cria outra lista com cinco nomes de usuários desejados, chamada `new_users`. Alguns desses nomes já estão na lista de usuários existentes.
3. Verifica se os nomes de `new_users` já estão sendo usados em `current_users`.
4. A comparação deve ser insensível a maiúsculas e minúsculas (por exemplo, `'John'` e `'JOHN'` devem ser considerados iguais).
5. Exibe uma mensagem informando se cada nome de usuário está disponível ou se o usuário deve escolher outro nome.

---

## Conceitos Utilizados

- **Listas**: Armazenamento de múltiplos nomes de usuários.
- **List Comprehension**: Para transformar todos os nomes de `current_users` para letras minúsculas.
- **Laços `for`**: Para iterar sobre os novos nomes de usuários.
- **Condicionais**: Para verificar se o nome já está sendo usado.
- **Manipulação de Strings**: Uso do método `.lower()` para tornar a comparação case-insensitive.

---

## Exemplo de Código

Aqui está o código utilizado:

```python
# Lista de usernames atuais
current_users = ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward']

# Lista de novos usernames
new_users = ['Charlie', 'Edward', 'Frank', 'Grace', 'Harry']

# Convertendo os usernames atuais para letras minúsculas
current_users_lower = [user.lower() for user in current_users]

# Verificando os novos usernames
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Desculpe, o nome de usuário '{new_user}' já está em uso. Por favor, escolha outro.")
    else:
        print(f"O nome de usuário '{new_user}' está disponível!")
