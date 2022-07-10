from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field

class Nutrients(BaseModel):
    calories : str = Field(...)
    carbohydrateContent: str = Field(...)
    cholesterolContent: str = Field(...)
    fatContent: str = Field(...)
    fiberContent: str = Field(...)
    proteinContent: str = Field(...)
    saturatedFatContent: str = Field(...)
    sodiumContent: str = Field(...)
    sugarContent: str = Field(...)


class RecipeSchema(BaseModel):
    recipe_name: str = Field(...)
    recipe_description: str = Field(...)
    recipe_image: str = Field(...)
    recipe_nutrients : Union[Nutrients, None] = None
    recipe_prep_time: int = Field(...)
    recipe_servings: str = Field(...)
    recipe_ingredients: list[str] = []
    recipe_procedure: str = Field(...)
    recipe_url: str = Field(...)




def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}