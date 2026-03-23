from sqlalchemy.orm import Session
from app.models.Product import Product
from app.schemas.products import ProductCreate
from app.schemas.products import ProductOut


class ProductsRepo:
    def __init__(self, db: Session):
        self.db = db

    def check_product_exists(self, product: ProductCreate) -> bool:
        return self.db.query(Product).filter(Product.name == product.name).first() is not None

    def create_product(self, product: ProductCreate) -> Product:
        db_product = Product(name=product.name, price=product.price, quantity=product.quantity)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_products(self) -> list[ProductOut]:
        return [ProductOut.model_validate(product) for product in self.db.query(Product).all()]

    def delete_product(self, product_id: int) -> bool:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False

    def get_product_by_id(self, product_id: int) -> ProductOut | None:
        return self.db.query(Product).filter(Product.id == product_id).first()
