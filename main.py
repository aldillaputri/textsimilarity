from fastapi import FastAPI
from pydantic import BaseModel
import cosine

app = FastAPI()

class CosineMaterial(BaseModel):
    text1: str
    text2: str
    base_grade: int


@app.post('/cosine/')
def cosine_grade(cosine_material: CosineMaterial):
    grade = cosine.calculate_grade(
        cosine_material.text1,
        cosine_material.text2,
        cosine_material.base_grade)
    return {'grade': grade}