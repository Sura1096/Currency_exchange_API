import uvicorn
from fastapi import FastAPI

from app.api.endpoints.users import auth_user_route
from app.api.endpoints.currency import currency_route


app = FastAPI()

app.include_router(auth_user_route)
app.include_router(currency_route)


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
