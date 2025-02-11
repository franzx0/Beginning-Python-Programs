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
