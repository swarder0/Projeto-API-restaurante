from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime,timezone, timedelta


class OrderItem(BaseModel):
    product_id: int = Field(..., description="ID of the product")
    quantity: int = Field(..., description="Quantity of the product")
    price: float = Field(..., description="Price of the product")
    total_price: float = Field(..., description="Total price of the order item")
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc), description="Creation timestamp of the order item")
    updated_at: datetime = Field(default_factory=datetime.now(timezone.utc), description="Last update timestamp of the order item")

    @field_validator("total_price")
    def validate_total_price(cls, value):
        if value < 0:
            raise ValueError("Total price must be a positive number.")
        return value
    
    @field_validator("quantity")
    def validate_quantity(cls, value):
        if value <= 0:
            raise ValueError("Quantity must be a positive integer.")
        return value

class OrderCreate(BaseModel):
    address: Optional[str]
    items: List[OrderItem]

class OrderDB(BaseModel):
    id: str
    address: Optional[str]
    items: List[OrderItem]
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc), description="Creation timestamp of the order")
    updated_at: datetime = Field(default_factory=datetime.now(timezone.utc), description="Last update timestamp of the order")
    status: str = Field(default="pending", description="Status of the order")