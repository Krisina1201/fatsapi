from pydantic import BaseModel

class shop(BaseModel):
    shop_id: int

class order(BaseModel):
    order_id: int

class product(BaseModel):
    product_id: int

