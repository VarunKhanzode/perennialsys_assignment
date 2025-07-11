from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.services.search_service import search_employees
from app.services.rate_limiter import rate_limiter
from app.models.models import load_sample_data
from app.core.logger import logger

router = APIRouter()

@router.get("/search")
def search(request: Request,
           status: str = None,
           search_key: str = "",
           department: str = None,
           location: str = None,
           position: str = None,
           page: int = 1,
           page_size: int = 10,
           org_id: int = 1,
           db: Session = Depends(get_db)):
    try:
        client_ip = request.client.host
        key = f"{org_id}:{client_ip}"
        if not rate_limiter.is_allowed(key):
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        return search_employees(status, search_key, department, location, position, page, page_size, org_id, db)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")

@router.post("/load-sample-data")
def load_data(db: Session = Depends(get_db)):
    load_sample_data(db)
    return {"message": "Sample data loaded"}
