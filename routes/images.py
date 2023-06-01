
from fastapi import APIRouter
import requests
from schemas.addFav import Favorites

images = APIRouter()
apiKey = "live_O68jyHNxQwYFpymmOKgmjQsNfzl00Zhlp3iVlf6QnJ1yBtiAP9oF6I3zj52ESv3F"
urlApi = "https://api.thecatapi.com/v1/"
header = {
            "Content-Type": "application/json"
          , "x-api-key": apiKey
          }

@images.get("/images/getImages")
def getTenImages():
    data = requests.get(f'{urlApi}images/search?limit=10&api_key=apiKey')
    if  data.status_code == 200:
        return data.json()
    else:
        return {"status": 400, "content": "error al obtener imagenes"}


@images.post("/images/addFav")
def addFav(fav: Favorites):
    createBody = {
                "image_id":fav.image_id,
                "sub_id": fav.sub_id
                }
    data = requests.post(f'{urlApi}favourites', json=createBody, headers=header)
    if data.status_code == 200:
        return {"status": 200, "content": "realizado con exito"}
    else:
         return {"status": 400, "content": "error al guardar favorito"}
    
@images.get("/images/getFavourites/{favoriteId}")
def getFavourites(favoriteId):
    data = requests.get(f"{urlApi}favourites?sub_id={favoriteId}", headers=header)
    if data.status_code == 200:
        return data.json()
    else:
        print(data)
        return {"status": 400, "content": "error al obtener favoritos"}