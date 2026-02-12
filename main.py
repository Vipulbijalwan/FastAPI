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


@app.put("/update_product/{product_id}")
def update_product(data:ProductDTO,product_id:int):
    for index,one_product in enumerate(products):
      if one_product.get("id") == product_id:
        products[index]=data.model_dump()
        
    return {"status": "Product updated successfully..."
            ,"data":data}
    
    
@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index,one_product in enumerate(products):
      if one_product.get("id") == product_id:
        delete_product=products.pop(index)
        return {"status": "Product deleted successfully..."
            ,"data":delete_product}
    return {"error": "Product not found"}