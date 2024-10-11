import requests
import json

def fetch_pokemon_data(pokemon_name):
    '''This function will retrieve the pokemon data from the pokeapi website.'''
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    try:
        # Get the response from the url and convert it to json data
        response = requests.get(url)
        json_data = response.text
        # Convert json to python
        all_data = json.loads(json_data)
        # Extract the ability names
        pokemon_abilities = [x['ability']['name'] for x in all_data["abilities"]]
        # Extract the data we want
        pokemon_data = {
            "name": all_data["name"],
            "type": all_data["types"][0]['type']['name'],
            "height": all_data["height"],
            "weight": all_data["weight"],
            "abilities": pokemon_abilities
        }
        return pokemon_data
    # Handle any exceptions like if someone inputs an incorrect pokemon name
    except Exception as e:
        print(f"Error: {e}")
        
def display_pokemon_data(pokemon_data):
    '''This function will display the pokemon data (name, type, height, weight, and abilities) in a  user-friendly format. '''
    try: 
        print(f'''
Name: {pokemon_data['name'].title()}
Type: {pokemon_data['type'].title()} 
Height: {pokemon_data['height']}
Weight: {pokemon_data['weight']}
Abilities: ''')
        for ability in pokemon_data['abilities']:
            print(f"- {ability.title()}")
    # Handling any exceptions like a non-compatible list of data
    except Exception as e: 
        print(f"Error: {e}")

def calculate_average_weight(pokemon_list):
    '''This function will calculate the average weight of the list of pokemon provided and return it.'''
    weight_list = []
    try: 
        # For each pokemon on the list
        for pokemon in pokemon_list:
            poke_data = fetch_pokemon_data(pokemon) # Fetch the data
            weight_list.append(int(poke_data['weight'])) # Pull out the weight
            display_pokemon_data(poke_data) # Display the data
        # Calculate the average by adding up the weights and dividing by the number of pokemon
        sum = 0
        for weight in weight_list:
            sum += weight
        average = sum/len(weight_list)
        return average # Return average of the pokemon
    # Handle any exceptions like an incorrect pokemon name
    except Exception as e:
        print(f"Error: {e}")

pokemon_list = ["pikachu", "bulbasaur", "charmander"]
average_weight = calculate_average_weight(pokemon_list)
print(f"\nThe average weight of the provided pokemon is: {average_weight:.2f}.")