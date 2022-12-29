import json


def get_all_names():
  pokemon = []
  f = open('pokedex.json')
  data = json.load(f)
  for i in range(len(data)):
    the_pokemon = data[i]
    pokemon_name = the_pokemon["name"]
    pokemon.append(pokemon_name["english"])
  return (pokemon)


def get_id(name):
  f = open('pokedex.json')
  data = json.load(f)
  for i in range(len(data)):
    the_pokemon = data[i]
    pokemon_name = the_pokemon["name"]
    if (pokemon_name["english"].lower() == name.lower()):
      return (the_pokemon["id"])


def get_stats(name):
  f = open('pokedex.json')
  data = json.load(f)
  for i in range(len(data)):
    the_pokemon = data[i]
    pokemon_name = the_pokemon["name"]
    if (pokemon_name["english"].lower() == name.lower()):
      return (the_pokemon["base"])


def get_type(name):
  f = open('pokedex.json')
  data = json.load(f)
  for i in range(len(data)):
    the_pokemon = data[i]
    pokemon_name = the_pokemon["name"]
    if (pokemon_name["english"].lower() == name.lower()):
      return (the_pokemon["type"])
