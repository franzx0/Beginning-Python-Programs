# Criando o dicionário cities
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is the largest metropolitan area in the world."
    },
    "New York": {
        "country": "USA",
        "population": "8.8 million",
        "fact": "New York is known as the 'Big Apple'."
    },
    "Paris": {
        "country": "France",
        "population": "2.2 million",
        "fact": "Paris is home to the famous Eiffel Tower."
    }
}

# Exibindo as informações de cada cidade
for city, details in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {details['country']}")
    print(f"Population: {details['population']}")
    print(f"Fact: {details['fact']}")
