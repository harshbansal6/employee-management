from datetime import timedelta

from passlib.hash import bcrypt
from fastapi import APIRouter, status, Depends, Query
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from app.depends.auth import authenticate_user, create_access_token
from app.serializers import schemas
from app.serializers.schemas import EmployeeOut
from core.depends import get_database
from app.depends import crud

router = APIRouter(tags=["Employee"])


@router.post("/employees", response_model=schemas.EmployeeOut, status_code=status.HTTP_201_CREATED)
def create_employee(employee: schemas.EmployeeCreate, session: Session = Depends(get_database), token: str = Depends(authenticate_user)):
    return crud.create_employee(session, employee)

@router.get("/employees", response_model=list[schemas.EmployeeOut])
def list_employees(
    session: Session = Depends(get_database),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=10),
    department: str = None,
    role: str = None,
    token: str = Depends(authenticate_user),
):
    employees = crud.get_employees(session, skip=skip, limit=limit, department=department, role=role)
    return [EmployeeOut.from_orm(emp) for emp in employees]

@router.get("/employees/{employee_id}", response_model=schemas.EmployeeOut)
def get_employee(employee_id: int, session: Session = Depends(get_database), token: str = Depends(authenticate_user)):
    db_employee = crud.get_employee(session, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return db_employee

@router.put("/employees/{employee_id}", response_model=schemas.EmployeeOut)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, session: Session = Depends(get_database), token: str = Depends(authenticate_user)):
    db_employee = crud.update_employee(session, employee_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return db_employee

@router.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int, session: Session = Depends(get_database), token: str = Depends(authenticate_user)):
    db_employee = crud.delete_employee(session, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")



@router.post("/register", response_model=schemas.UserCreate, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, session: Session = Depends(get_database)):
    if crud.get_user_by_username(session, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    return crud.create_user(session, user)

@router.post("/login", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_database)):
    user = crud.get_user_by_username(session, form_data.username)
    if not user or not bcrypt.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}