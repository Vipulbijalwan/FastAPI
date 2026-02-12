from pydantic import BaseModel 


class ProductDTO(BaseModel):
    id: int
    title: str
    price: float =0.0
    count: int