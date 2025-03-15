import requests
import base64
import keyspfy


CLIENT_ID = "4c83e057c83c48bcbf604ae1f63f52f9"
CLIENT_SECRET = keyspfy.CLIENT_SECRET

def get_token() -> str:
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers= headers, data= data)

    if response.status_code != 200:
        raise Exception(f"Error obteniendo el token de Spotify : {response.json()}")
    
    return response.json()["access_token"]

def buscar_Artista(token: str, nombre: str):
    url = f"https://api.spotify.com/v1/search?q={nombre}&type=artist&limit=1"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo el artista: {response.json()}."
        )

    results = response.json()
    if results["artists"]["items"]:
        return results["artists"]["items"][0]["id"]
    else:
        raise Exception(
            f"El artista {nombre} no se ha encontrado."
        )
    
def get_Artista_datos(token: str, id: str):
    url = f"https://api.spotify.com/v1/artists/{id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo los datos del artista: {response.json()}."
        )

    results = response.json()
    return {
        "Nombre" : results["name"],
        "Seguidores" : results["followers"]["total"],
        "Popularidad" : results["popularity"]
    }

def get_Artista_Cancion_Top(token: str, id: str):
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo las canciones del artista: {response.json()}."
        )
    
    results = response.json()
    cancion_top = max(results["tracks"] , key=lambda x: x["popularity"])
    return {
        "Nombre" : cancion_top["name"],
        "Popularidad" : cancion_top["popularity"]
    }


# 1. Obtener un token
token = get_token()


# 2. Obtener los IDs de los artistas

print("¡Bienvenido a la comparaciones de artistas.!\n")
nombreartista = str(input("Coloca el nombre del primer artista: ")).lower().capitalize()
nombreartista2 = str(input("Coloca el nombre del segundo artista: ")).lower().capitalize()



artista_id_1 = buscar_Artista(token, nombreartista)
artista_id_2 = buscar_Artista(token, nombreartista2)


# 3. Datos

# 3.1 Esto es nombre del artista, popularidad y seguidores.
artista1 = get_Artista_datos(token, artista_id_1)
artista2 = get_Artista_datos(token, artista_id_2)

# 3.2 Esto es la cancion mas popular
cancion_top_artista_1 = get_Artista_Cancion_Top(token, artista_id_1)
cancion_top_artista_2 = get_Artista_Cancion_Top(token, artista_id_2)


contador_ganado_1 = 0
contador_ganado_2 = 0

# 4. Comparar los resultados de cada artista

print(f"¡Comparacion de artistas!")
print(f"\n{artista1["Nombre"]} es el primer artista")
print(f"{artista2["Nombre"]} es el segundo artista")


# 4.1 Comparacion de seguidores
print(f"\nComparacion de seguidores:")
print(f"{artista1["Nombre"]} tiene {artista1["Seguidores"]} seguidores.")
print(f"{artista2["Nombre"]} tiene {artista2["Seguidores"]} seguidores.")

if artista1["Seguidores"] > artista2["Seguidores"]:
    print(f"{artista1['Nombre']} tiene mas seguidores.")
    contador_ganado_1 += 1
elif artista1["Seguidores"] == artista2["Seguidores"]:
    print(f"Tienen los mismos seguidores")
else:
    print(f"{artista2['Nombre']} tiene mas seguidores.")
    contador_ganado_2 += 1

# 4.2 Comparacion de popularidad
print(f"\nComparacion de popularidad:")
print(f"{artista1["Nombre"]}: {artista1["Popularidad"]}")
print(f"{artista2["Nombre"]}: {artista2["Popularidad"]}")

if artista1["Popularidad"] > artista2["Popularidad"]:
    print(f"{artista1['Nombre']} tiene mas popularidad en general.")
    contador_ganado_1 += 1
elif artista1["Popularidad"] == artista2["Popularidad"]:
    print(f"Tienen la misma popularidad")
else:
    print(f"{artista2['Nombre']} tiene mas popularidad en general.")
    contador_ganado_2 += 1

# 4.3 Comparacion de Cancion Top
print(f"\nComparacion de cancion:")
print(f"Cancion de {artista1["Nombre"]}: {cancion_top_artista_1["Nombre"]}, Popularidad: {cancion_top_artista_1["Popularidad"]}")
print(f"Cancion de {artista2["Nombre"]}: {cancion_top_artista_2["Nombre"]}, Popularidad: {cancion_top_artista_2["Popularidad"]}")

if cancion_top_artista_1["Popularidad"] > cancion_top_artista_2["Popularidad"]:
    print(f"La cancion: {cancion_top_artista_1['Nombre']} de {artista1['Nombre']} es mas popular")
    contador_ganado_1 += 1
elif cancion_top_artista_1["Popularidad"] == cancion_top_artista_2["Popularidad"]:
    print(f"Las canciones: {cancion_top_artista_1['Nombre']} y {cancion_top_artista_2['Nombre']} son igual de populares")
else:
    print(f"La cancion: {cancion_top_artista_2['Nombre']} de {artista2['Nombre']} es mas popular")
    contador_ganado_2 += 1

# 5. Resultado final

print(f"\nRESULTADO FINAL:")
if contador_ganado_1 > contador_ganado_2:
    print(f"{artista1['Nombre']} en terminos generales es mas popular que {artista2['Nombre']}")
else:
    print(f"{artista2['Nombre']} en terminos generales es mas popular que {artista1['Nombre']}")