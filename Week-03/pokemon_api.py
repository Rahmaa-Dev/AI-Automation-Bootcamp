import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

pokemon = response.json()

print("Name:", pokemon["name"])
print("Height:", pokemon["height"])
print("Weight:", pokemon["weight"])
print("Base Experience:", pokemon["base_experience"])
print("Abiliti 1:", pokemon["abilities"][0]["ability"]["name"])
print("Ability 2:", pokemon["abilities"][1]["ability"]["name"])