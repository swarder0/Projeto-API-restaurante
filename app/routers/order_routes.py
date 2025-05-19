from fastapi import APIRouter, Depends
from typing import List
from app.crud.order import get_orders_by_user
from app.service.dependencies import get_current_user
from app.models.order import OrderCreate, OrderDB

router = APIRouter(prefix="/orders", tags=["Pedidos"])

@router.post("/", response_model=OrderDB)
async def create_order(
    order: OrderCreate,
    current_user: dict = Depends(get_current_user)
):
    created_order = await create_order(user_id=current_user["_id"], order=order)
    return created_order

@router.get("/", response_model=List[OrderDB])
async def list_orders(current_user: dict = Depends(get_current_user)):
    orders = await get_orders_by_user(current_user["_id"])
    return orders
