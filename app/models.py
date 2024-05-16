from datetime import datetime

from pydantic import BaseModel

class shop(BaseModel):
    shop_id: int
    shop_name: str
    address: str
    phone_number: str
    last_name_of_the_manager: str
    first_name_of_the_concat_person: str

class order(BaseModel):
    order_id: int
    shop_id: int
    product_id: int
    count_product: int
    data: datetime

class product(BaseModel):
    product_id: int
    product_name: int
    product_count: int
    price: int

