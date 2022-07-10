from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_recipe,
    retrieve_recipes,
    retrieve_recipe
)

from app.server.models.recipe import (
    ErrorResponseModel,
    ResponseModel,
    RecipeSchema,
)

router = APIRouter()


@router.get("/", response_description="Recipes retrieved")
async def get_recipess():
    recipes = await retrieve_recipes()
    if recipes:
        return ResponseModel(recipes, "Recipes data retrieved successfully")
    return ResponseModel(recipes, "Empty list returned")


@router.get("/{id}", response_description="Recipe data retrieved")
async def get_recipe_data(id):
    recipe = await retrieve_recipe(id)
    if recipe:
        return ResponseModel(recipe, "Recipe data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Recipe doesn't exist.")



@router.post("/", response_description="Recipe data added into the database")
async def add_srecipedata(recipe: RecipeSchema = Body(...)):
    recipe = jsonable_encoder(recipe)
    new_recipe = await add_recipe(recipe)
    return ResponseModel(new_recipe, "Recipe added successfully.")