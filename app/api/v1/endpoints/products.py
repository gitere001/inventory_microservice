from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.products import ProductOut, ProductCreate
from app.services.product_service import ProductService
from fastapi import status

router = APIRouter()


@router.get("/all", response_model=list[ProductOut])
async def get_products(db: Session = Depends(get_db)):
    return ProductService(db).get_products()


@router.post("/create", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return ProductService(db).create_product(product)


@router.delete("/delete/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService(db).delete_product(product_id)


@router.get("/single/{product_id}", status_code=status.HTTP_200_OK)
async def get_single_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService(db).get_single_product(product_id)
