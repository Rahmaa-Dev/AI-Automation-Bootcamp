import requests


def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower().strip()}"

    response = requests.get(url)

    if response.ok:
        return response.json()

    return None


pokemon_name = input("Enter Pokémon: ")

pokemon = get_pokemon(pokemon_name)

if pokemon:
    print(f"\nName: {pokemon['name'].title()}")
else:
    print("Pokémon not found.")