import requests

def fetch_planet_data():
    '''This function fetches the name, mass, and orbit period for each planet and returns a list of dictionaries.'''
    # Generate the request and extract the planet data
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    # The planet list will be a list of dictionaries with the key values "name", "mass", and "orbit" corresponding to their values
    planet_list = []
    # Iterate over each body in the database
    for body in planets:
        # Only include planes
        if body['isPlanet']:
            name = body['englishName']         # Extract English Name
            mass = body['mass']['massValue']   # Extract Mass Value
            orbit_period = body['sideralOrbit'] # Extract the Orbit Period
            planet_list.append({
                "name": name,
                "mass": mass,
                "orbit": orbit_period
            })
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planet_list

# def find_heaviest_planet(planet_list):
#     '''This function takes takes the list of planets, finds the planet with the heaviest mass and returns it.'''
#     mass_list = []
#     for planet in planet_list:
#         mass_list.append(float(planet['mass']))
#     heaviest = max(mass_list)
#     for planet in planet_list:
#         if planet['mass']==heaviest:
#             print(f"The heaviest planet is {planet['name']} with a mass of {planet['mass']:.2f}.")
#             return planet
    
def find_heaviest_planet(planet_list):
    '''This function takes takes the list of planets, finds the planet with the heaviest mass and returns it.'''
    heaviest_planet = planet_list[0]
    # For each planet, compare the mass to the current heaviest. If bigger, make heaviest
    for planet in planet_list:
        if (float(heaviest_planet['mass'])<=float(planet['mass'])):
            heaviest_planet = planet
    # Return heaviest planet
    return heaviest_planet['name'], heaviest_planet['mass']

planet_list = fetch_planet_data()
name, mass = find_heaviest_planet(planet_list)
print(f"The heaviest planet is {name} with a mass of {mass:.2f}.")       
