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
