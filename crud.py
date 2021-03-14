from sqlalchemy.orm import Session

import models, schemas


def get_product(db: Session):
    return db.query(models.Product).all()


def create_user(db: Session, user: schemas.ProductCreate):
    
    db_user = models.Product(name=user.name, price=user.price)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user