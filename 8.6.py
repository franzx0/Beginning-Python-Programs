def city_country(cidade, pais):
    """Retorna uma string no formato 'Cidade, País'."""
    return f"{cidade.title()}, {pais.title()}"

# Chamadas da função com diferentes pares cidade-país
print(city_country('santiago', 'chile'))
print(city_country('rio de janeiro', 'brasil'))
print(city_country('nova york', 'estados unidos'))
