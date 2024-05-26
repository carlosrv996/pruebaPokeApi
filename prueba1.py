import requests

def obtener_informacion_pokemon(nombre_pokemon):
    
    # Construye la URL para la API con el nombre en minúsculas.
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)
    
    # Verifica si la respuesta es exitosa (código de estado 200).
    if response.status_code == 200:
        data = response.json()

        # Obtiene los tipos y habilidades y los convierte en una lista.
        nombre = data['name'].capitalize()
        tipos = [tipo['type']['name'] for tipo in data['types']]
        habilidades = [habilidad['ability']['name'] for habilidad in data['abilities']]
        print(f"Nombre: {nombre}")
        print(f"Tipo(s): {', '.join(tipos)}")
        print(f"Habilidades: {', '.join(habilidades)}")
    else:
        print("¡El Pokémon no fue encontrado!")

if __name__ == "__main__":
    
    # Solicita al usuario que ingrese el nombre.
    nombre_pokemon = input("Ingresa el nombre del Pokémon: ")
    # Llama a la función 'obtener_informacion_pokemon' con el nombre del ingresado.
    obtener_informacion_pokemon(nombre_pokemon)
