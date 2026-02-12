from mockproduct import products
from fastapi import FastAPI, Request
from dtos import ProductDTO

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


# Get all products
@app.get("/products")
def get_products():
    return products


# Path parameter
@app.get("/products/{product_id}")
def get_one_product(product_id: int):
    for one_product in products:
        if one_product.get("id") == product_id:
            return one_product
    
    return {"error": "Product not found"}


# Query parameter
@app.get("/greet")
def greet_user(request: Request):
    params = dict(request.query_params)
    name = params.get("name", "Guest")   # default value added
    return {"message": f"Hello {name}"}


# POST method
@app.post("/create_product")
def create_product(data:ProductDTO):
    product_data=data.model_dump()
    products.append(product_data)
    return {"status": "Product created successfully..."
            ,"data":products}
