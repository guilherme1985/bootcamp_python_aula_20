from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductUpdate
from models import ProductModel

# get all (select * from)
def get_products(db: Session):
    """ Retorna todos os produtos """
    return db.query(ProductModel).all()

# get where id = ?
def get_product(db: Session, product_id: int):
    """ Retorna um produto pelo ID """
    return db.query(ProductModel).filter(ProductModel.id == product_id)

# insert into
def create_product(db: Session, product: ProductCreate):
    """ Cria um novo produto """

    # transforma a view para ORM
    db_product = ProductModel(**product.model_dump())

    # adicionar na tabela
    db.add(db_product)

    # commitar na tabela
    db.commit()

    # fazer refresh do banco de dados
    db.refresh(db_product)

    # retornar o produto criado
    return db_product

# delete where id = ?
def delete_product(db: Session, product_id: int):
    """ Deleta um produto pelo ID """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product

# update where id = ?
def update_product(db: Session, product_id: int, product: ProductUpdate):
    """ Atualiza um produto pelo ID """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name
    
    if product.description is not None:
        db_product.description = product.description
    
    if product.price is not None:
        db_product.price = product.price
    
    if product.categoria is not None:
        db_product.categoria = product.categoria
    
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    db.refresh(db_product)
    return db_product
