#import the packages we need:
import requests, json

def pokemon_dict(pokemon):
    #retrieves from the internet the information
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    pokemon_data = requests.get(url)
    #creates a list of stats
    pokemon_stat_list = []
    for ele in pokemon_data.json()["stats"]:
        pokemon_stat_list.append(f'{ele["stat"]["name"]} {ele["base_stat"]}')
    #retreives the types from the list of types   
    pokemon_type = ""
    for ele in pokemon_data.json()["types"]:
        pokemon_type += f'{ele["type"]["name"]} '
    
    #Makes the dictionary to be returned
    guide = {
        "name": f'{pokemon}',
        "Pokemon Ability": pokemon_data.json()["abilities"][0]["ability"]["name"],
        "Pokemon Base Exp": pokemon_data.json()["base_experience"],
        "Pokemon shiny front sprites":pokemon_data.json()['sprites']['front_shiny'],
        "Pokemon Wieght":pokemon_data.json()["weight"],
        "Pokemon Stat List":pokemon_stat_list,
        "Pokemon Types": pokemon_type.strip()
              
        
    }
    return guide

list_pokemon = ["squirtle","blastoise","caterpie","raichu","jigglypuff",
                "ivysaur","ninetales","clefairy","pikachu","bulbasaur",
                "venusaur","pidgey","charmeleon","wartortle","rattata",
                "fearow", "charizard","mewtwo","mew","zapdos"]
all_pokemon = {}
for pokemon_name in list_pokemon:
    name = pokemon_dict(pokemon_name)["name"]
    info = {
        "wieght":pokemon_dict(pokemon_name)["Pokemon Wieght"],
        "stat list":pokemon_dict(pokemon_name)["Pokemon Stat List"],
        "abilities":pokemon_dict(pokemon_name)["Pokemon Ability"],
        "pokemon base exp":pokemon_dict(pokemon_name)["Pokemon Base Exp"],
        "pokemon shiny front sprites":pokemon_dict(pokemon_name)["Pokemon shiny front sprites"]
        
    }
    all_pokemon[name] = info
type_dict = {}
for pokemon_name in list_pokemon:
    type_pokemon = pokemon_dict(pokemon_name)["Pokemon Types"]
    if type_pokemon not in type_dict:
        type_dict[type_pokemon] = {}
    type_dict[type_pokemon][pokemon_name] = all_pokemon[pokemon_name]

print(type_dict)
print(type_dict["water"])
print(type_dict["fire"])
