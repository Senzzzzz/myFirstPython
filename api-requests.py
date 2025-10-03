import requests

base_url = "https://dattebayo-api.onrender.com"

api = ""
city = ""
url = base_url + api + city
def get_naruto_data(id):
    naruto_url = f"{base_url}/characters/{id}"
    response = requests.get(naruto_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)


naruto_characters_id = 1
naruto_characters_info = get_naruto_data(naruto_characters_id)
print(naruto_characters_info["name"])
