from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductCreate, ProductResponse, ProductUpdate
from typing import List
from crud import create_product, get_products, get_product, delete_product, update_product

router = APIRouter()

### criar rota para buscar todos os itens
### sempre vamos ter 2 atributos, PATH e o RESPONSE
@router.get("/products/", response_model=List[ProductResponse])
def read_all_product(db: Session = Depends(get_db)):
    """Retorna todos os produtos"""
    products = get_products()
    return products

### criar rota de buscar 1 item
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_all_product(product_id: int, db: Session = Depends(get_db)):
    """Retorna um produto"""
    db_product = get_product(db = db, product_id = product_id)
    if db_product is None:
        raise HTTPException(status_code = 404, detail = f"Produto {product_id}, não existe!")
    return db_product


### criar rota para criar um produto
@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product=product, db=db)

### criar rota para deletar um produto
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code = 404, detail = f"Produto {product_id}, não existe!")
    return product_db
    

### criar rota para atualizar um produto
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code = 404, detail = f"Produto {product_id}, não existe!")
    return product_db