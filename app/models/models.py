from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    department = Column(String)
    location = Column(String)
    position = Column(String)
    status = Column(String)
    organization_id = Column(Integer, index=True)

class OrganizationConfig(Base):
    __tablename__ = "organization_configs"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, unique=True)
    visible_columns = Column(String)  # Comma-separated values


def load_sample_data(db):
    if db.query(Employee).count() == 0:

        employees = [
            Employee(name=f"Employee{i}", 
                    email=f"employee{i}@org{(i % 5) + 1}.com", 
                    phone=f"{1000 + i}", 
                    department=["HR", "Engineering", "Support", "Sales", "Finance"][i % 5], 
                    location=["NY", "SF", "TX", "LA", "CHI"][i % 5], 
                    position=["Manager", "Dev", "Agent", "Lead", "Analyst"][i % 5], 
                    status=["Active", "Not Started", "Terminated"][(i % 3)],
                    organization_id=(i % 5) + 1
            )
            for i in range(1, 51)
]

        org_configs = [
            OrganizationConfig(organization_id=1, visible_columns="name,email,phone,department,status"),
            OrganizationConfig(organization_id=2, visible_columns="name,location,position,status"),
            OrganizationConfig(organization_id=3, visible_columns="name,email,location,department,position"),
            OrganizationConfig(organization_id=4, visible_columns="name,phone,position,status"),
            OrganizationConfig(organization_id=5, visible_columns="name,email,phone,status")
]



        # db.add_all(employees + [config1, config2])
        db.add_all(employees + org_configs)
        db.commit()
