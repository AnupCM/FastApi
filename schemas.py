from typing import List
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int


class ProductCreate(ProductBase):
    price: int


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True