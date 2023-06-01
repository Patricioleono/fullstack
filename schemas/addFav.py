from pydantic import BaseModel

class Favorites(BaseModel):
    image_id: str
    sub_id: str