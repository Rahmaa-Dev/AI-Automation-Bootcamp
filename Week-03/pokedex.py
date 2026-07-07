import requests

pokemon_name = input("Enter a Pokémon name: ").lower().strip()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

response = requests.get(url)

if response.ok:
    pokemon = response.json()

    print(f"\nName: {pokemon['name'].title()}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")

    print("\nAbilities:")
    for ability in pokemon["abilities"]:
        print(f"- {ability['ability']['name']}")

else:
    print(f"❌ '{pokemon_name}' was not found.")