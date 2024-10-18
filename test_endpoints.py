import requests

def test_get_players():
    url = "http://127.0.0.1:8000/players/?skip=0&limit=10"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"GET Players - Success: {response.json()}")
    else:
        print(f"GET Players - Failed: {response.status_code}, {response.json()}")

def test_create_player():
    url = "http://127.0.0.1:8000/players/"
    player_data = {"name": "Test Player", "height": 180}
    response = requests.post(url, json=player_data)
    
    if response.status_code == 200:
        print(f"POST Player - Success: {response.json()}")
    else:
        print(f"POST Player - Failed: {response.status_code}, {response.json()}")

def test_get_players_after_post():
    # Crear un jugador
    url_post = "http://127.0.0.1:8000/players/"
    player_data = {"name": "New Player", "height": 185}
    post_response = requests.post(url_post, json=player_data)
    
    if post_response.status_code == 200:
        print(f"POST Player - Success: {post_response.json()}")
    else:
        print(f"POST Player - Failed: {post_response.status_code}, {post_response.json()}")

    # Hacer un GET después de crear el jugador
    url_get = "http://127.0.0.1:8000/players/?skip=0&limit=10"
    get_response = requests.get(url_get)

    if get_response.status_code == 200:
        print(f"GET Players after POST - Success: {get_response.json()}")
    else:
        print(f"GET Players after POST - Failed: {get_response.status_code}, {get_response.json()}")

if __name__ == "__main__":
    test_get_players()
    test_create_player()
    test_get_players_after_post()
