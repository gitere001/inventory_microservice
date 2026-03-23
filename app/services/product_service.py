from app.repositories.products_repo import ProductsRepo
from app.schemas.products import ProductCreate
from fastapi import HTTPException, status


class ProductService:
    def __init__(self, db):
        self.repo = ProductsRepo(db)

    def get_products(self):
        return self.repo.get_products()

    def create_product(self, product_data: ProductCreate):
        if self.repo.check_product_exists(product_data):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product with this name already exists",
            )
        return self.repo.create_product(product_data)

    def delete_product(self, product_id: int):
        if not self.repo.delete_product(product_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )
        return {"detail": "Product deleted successfully"}

    def get_single_product(self, product_id: int):

        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        return product
