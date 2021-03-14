
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
import models, schemas, crud
from database import engine, SessionLocal

app = FastAPI()

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/product", response_model=schemas.Product)
def read_items(db: Session = Depends(get_db)):
    items = crud.get_product(db)
    return items
      

@app.post("/product", response_model=schemas.Product)
def create_user(name: str, tenure:int, interest: int,  db: Session = Depends(get_db)):
    getData = db.query(models.Product).filter(models.Product.name == name).first()
    interest1 = interest/(12.00 * 100.00) #one month interest
    tenure1 = tenure * 12.00 #one month period
    emi = (getData.price * interest1 * pow(1.00 + interest1, tenure1)) / (pow(1 + interest1, tenure1) - 1.00)
    return emi
