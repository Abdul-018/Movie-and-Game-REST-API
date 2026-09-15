from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

app = FastAPI(title="Movies & Games Vault API", version="1.0")

class MediaItem(BaseModel):
    title: str = Field(..., examples=["Spider Man: Brand New Day"])
    type: Literal["movie", "game"] = Field(..., examples = ["movie"])
    release_year: int = Field(..., ge=1888, le=2030, examples=[2010])
    genre: str = Field(..., examples = ["Fantasy"])
    rating: Optional[float] = Field(None, ge=0.0, le=10.0, examples=[8.8])

class MediaResponse(MediaItem):
    id: int

db: List[dict] = [
    {
        "id": 1,
        "title": "Kabhi Khushi Kabhi Gham",
        "type": "movie",
        "release_year": 2001,
        "genre": "Romance",
        "rating": 9.5
    },
    {
        "id": 2,
        "title": "Fortnite",
        "type": "game",
        "release_year": 2017,
        "genre": "Action",
        "rating": 7.5
    }
]
@app.get("/items", response_model=List[MediaResponse])
def get_items(item_type: Optional[Literal["movie", "game"]] = None):
    if item_type:
        return [item for item in db if item["type"] == item_type]
    return db

#@app.get("/items", response_model=List[MediaResponse])
#def get_items(item_rating: Optional[float]):
#    for item in db:
#        if item["rating"] >=

@app.get("/items/{item_id}", response_model=List[MediaResponse])
def get_items(item_id: int):
    for item in db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item not found")
    
@app.post("/items", response_model=MediaResponse)
def create_item(item: MediaItem):
    new_id = max([i["id"] for i in db], default=0) + 1
    new_item = {"id": new_id, **item.model_dump()}
    db.append(new_item)
    return new_item

@app.put("/item/{item_id}", response_model=List[MediaItem])
def update_item(item_id: int, updated_item: MediaItem):
    for idx, item in enumerate(db):
        if item["id"] == item_id:
            data = {"id": item_id, **update_item.model_dump()}
            db[idx] = data
            return data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.delete("/item/{item_id}", response_model=List[MediaItem])
def delete_item(item_id: int):
    for idx, item in enumerate(db):
        if item["id"] == item_id:
            deleted = db.pop(idx)
            return {"message": f"Deleted '{deleted['title']}' from vault"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
