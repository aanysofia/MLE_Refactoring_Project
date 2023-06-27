from fastapi import Depends, FastAPI, HTTPException
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"data": "KingCounty data"}

# get all kingcounty data
@app.get("/kingcountydata", response_model=list[schemas.KCOut])
def get_all_housedata(db: Session = Depends(get_db)):
    kcdata = db.query(models.KCdata).all()
    if not kcdata:
        raise HTTPException(status_code=404, detail="KCdata not found")
    return kcdata

# add kingcounty data
@app.post("/kingcountydata", response_model=schemas.KCOut)
def create_housedata(request: schemas.KCModel, db: Session = Depends(get_db)):
    new_kcdata = models.KCdata(price=request.price, bedrooms=request.bedrooms, bathrooms=request.bathrooms, sqft_living=request.sqft_living)
    db.add(new_kcdata)
    db.commit()
    db.refresh(new_kcdata)
    return new_kcdata

# update kingcounty data
@app.put("/kingcountydata/{id}")
def update_housedata(id: int, request: schemas.KCUpdate, db: Session = Depends(get_db)):
    kcdata = db.query(models.KCdata).filter(models.KCdata.id == id)
    if not kcdata.first():
        raise HTTPException(status_code=404, detail="KCdata not found")
    kcdata.update(request.dict())
    db.commit()
    return "Updated successfully"

# delete kingcounty data
@app.delete("/kingcountydata/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    kcdata = db.query(models.KCdata).filter(models.KCdata.id == id)
    if not kcdata.first():
        raise HTTPException(status_code=404, detail="KCdata not found")
    kcdata.delete(synchronize_session=False)
    db.commit()
    return "Deleted successfully"
