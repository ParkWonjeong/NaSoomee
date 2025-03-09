from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from pymongo import MongoClient
from bson import ObjectId
import shutil
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# MongoDB 연결
client = MongoClient(os.getenv("MONGO_URI"))
db = client.nasoomee
collection = db.artworks

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 작품 추가 API
@app.post("/api/artworks")
def upload_artwork(title: str = Form(...), description: str = Form(...), image: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{image.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    artwork = {"title": title, "description": description, "image": file_path}
    result = collection.insert_one(artwork)
    return {"id": str(result.inserted_id), "message": "작품 추가 완료"}

# 작품 목록 조회 API
@app.get("/api/artworks")
def get_artworks():
    artworks = []
    for artwork in collection.find():
        artworks.append({"id": str(artwork["_id"]), "title": artwork["title"], "description": artwork["description"], "image": artwork["image"]})
    return artworks

# 작품 삭제 API
@app.delete("/api/artworks/{artwork_id}")
def delete_artwork(artwork_id: str):
    result = collection.delete_one({"_id": ObjectId(artwork_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="작품을 찾을 수 없음")
    return {"message": "작품 삭제 완료"}

# 서버 실행 명령: uvicorn main:app --reload
