from datetime import datetime, timezone
from app.db.database import db
from bson import ObjectId

from app.models.order import OrderCreate


async def create_order(user_id: str, order_data: OrderCreate):
   order_dict = order_data.dict()
   order_dict.update({
      "user_id": user_id,
      "status": "pending",
      "created_at": datetime.now(timezone.utc),}
)
   result = await db.orders.insert_one(order_dict)
   create_order = await db.orders.find_one({"_id": result.inserted_id})
   create_order["_id"] = str(create_order["_id"])
   return create_order

async def get_orders_by_user(user_id: str):
    cursor = db.orders.find({"user_id": user_id})
    orders = []
    async for order in cursor:
        order["_id"] = str(order["_id"])
        orders.append(order)
    return orders