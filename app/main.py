from typing import Union

from fastapi import FastAPI, Depends

from app.app.db import User, database

app = FastAPI()



@app.post('/users/add')
async def add(user: User):
    return await user.save()

@app.get("/")
async def read_root():
    return await User.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()