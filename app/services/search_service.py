from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import or_
from app.models.models import Employee, OrganizationConfig
from app.core.logger import logger

def search_employees(status, search_key, department, location, position, page, page_size, org_id, db: Session):
    try:
        query = db.query(Employee).filter(Employee.organization_id == org_id)

        if status:
            query = query.filter(Employee.status == status)
        if search_key:
            query = query.filter(or_(
                Employee.name.ilike(f"%{search_key}%"),
                Employee.email.ilike(f"%{search_key}%"),
                Employee.phone.ilike(f"%{search_key}%")
            ))
        if department:
            query = query.filter(Employee.department == department)
        if location:
            query = query.filter(Employee.location == location)
        if position:
            query = query.filter(Employee.position == position)

        offset = (page - 1) * page_size
        results = query.offset(offset).limit(page_size).all()

        config = db.query(OrganizationConfig).filter_by(organization_id=org_id).first()
        columns = config.visible_columns.split(",") if config else []

        response = []
        for emp in results:
            row = {}
            for col in columns:
                row[col] = getattr(emp, col, None)
            response.append(row)

        if not response:
            raise HTTPException(status_code=404, detail="Data not found")
        return response
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")
