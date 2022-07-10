from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb+srv://Groot:groot1234@masterchefcluster.yb0sbgj.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database1 = client.students

student_collection = database1.get_collection("students_collection")

database2 = client.MC_DB

recipe_collection = database2.get_collection("MC_Collection")


# helpers


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }


def recipe_helper(recipe) -> dict:
    return {
        "id": str(recipe["_id"]),
        "recipe_name": recipe["recipe_name"],
        "recipe_description": recipe["recipe_description"],
        "recipe_image": recipe["recipe_image"],
        "recipe_nutrients": recipe["recipe_nutrients"],
        "recipe_prep_time": recipe["recipe_prep_time"],
        "recipe_ingredients": recipe["recipe_ingredients"],
        "recipe_procedure": recipe["recipe_procedure"],
        "recipe_url": recipe["recipe_url"],
    }

# Retrieve all recipes present in the database
async def retrieve_recipes():
    recipes = []
    async for recipe in recipe_collection.find():
        recipes.append(recipe_helper(recipe))
    return recipes


    # Retrieve a recipe with a matching ID
async def retrieve_recipe(id: str) -> dict:
    recipe = await recipe_collection.find_one({"_id": ObjectId(id)})
    if recipe:
        return recipe_helper(recipe)


# Add a new student into to the database
async def add_recipe(recipe_data: dict) -> dict:
    recipe = await recipe_collection.insert_one(recipe_data)
    new_recipe = await recipe_collection.find_one({"_id": recipe.inserted_id})
    return recipe_helper(new_recipe)


# Delete a student from the database
async def delete_recipe(id: str):
    recipe = await recipe_collection.find_one({"_id": ObjectId(id)})
    if recipe:
        await recipe_collection.delete_one({"_id": ObjectId(id)})
        return True