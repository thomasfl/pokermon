from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/user",
    tags=["user data"],
    responses={404: {"description": "Not found"}},
)

users = [
    {"username": "Thomas"},
    {"username": "Anniken"}
]

@router.get("/users")
async def get_user():
    return users

@router.post("/user")
async def create_user(username: str):
    print("create user ==> " + username)
    users.append({"username": username})
    return {"status": "ok"}

