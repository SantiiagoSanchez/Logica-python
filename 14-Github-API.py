import requests

def reporte_github(usuario: str):
    url_base = "https://api.github.com"

    url_usuario = f"{url_base}/users/{usuario}"

    datos_usuario = requests.get(url_usuario).json()

    if "status" in datos_usuario and datos_usuario["status"] == "404":
        print(f"ERROR: El usuario {usuario} no se ha encontrado.")
        return

    reporte = {
        "Nombre" : datos_usuario.get("name", "Desconocido"),
        "Compania" : datos_usuario.get("company", "Desconocida"),
        "Repositorios publicos" : datos_usuario.get("public_repos", 0),
        "Seguidores" : datos_usuario.get("followers", 0),
        "Seguidos" : datos_usuario.get("following", 0),
        "Mail" : datos_usuario.get("email", "Desconocido")
    }

    print(f"Informe del usuario '{usuario}'")
    for key, value in reporte.items():
        print(f"{key}: {value}")
    

    url_repositorios = datos_usuario["repos_url"]
    datos_repositorios = requests.get(url_repositorios).json()
    
    lenguajes = {}

    for repo in datos_repositorios:
        language = repo.get("language")
        if language:
            if language in lenguajes:
                lenguajes[language] += 1
            else:
                lenguajes[language] = 1
        print(f"\nRepo: {repo.get("full_name")}")
        print(f"Estrellas: {repo.get("stargazers_count", 0)}")
        print(f"Forks: {repo.get("forks_count", 0)}")
        
    lenguaje_mas_usado = None
    max_count = 0

    for nombre_lenguaje, contador_lenguaje in lenguajes.items():
        if contador_lenguaje > max_count:
            lenguaje_mas_usado = nombre_lenguaje
            max_count = contador_lenguaje

    print(f"\nLenguaje mas usado: {lenguaje_mas_usado}" if lenguaje_mas_usado else "Desconocido")
    print(lenguajes)


usuario = input("Introduce tu nombre de usuario en Github: ")
reporte_github(usuario)

