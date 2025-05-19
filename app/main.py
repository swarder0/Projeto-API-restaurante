from fastapi import FastAPI
from app.routers import user_routes, menu_routes, order_routes


app = FastAPI(

)

app.include_router(user_routes.router, prefix="/api/v1")
# app.include_router(menu_routes.router)
app.include_router(order_routes.router, prefix="/api/v1")

@app.get("/")
def root():
    return{"message": "API do restaurente is ON"}