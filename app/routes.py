from fastapi import APIRouter
from app import dal

router = APIRouter()


@router.get("/")
def get_engineering_high_salary_employees():
    return dal.get_engineering_high_salary_employees() 

@router.get("/")
def get_employees_by_age_and_role():
    return dal.get_employees_by_age_and_role()

@router.get("/")
def get_top_seniority_employees_excluding_hr():
    return dal.get_top_seniority_employees_excluding_hr()

@router.get("/")
def get_employees_by_age_or_seniority():
    return dal.get_employees_by_age_or_seniority()

@router.get("/")
def get_managers_excluding_departments():
    return dal.get_managers_excluding_departments()

@router.get("/")
def get_employees_by_lastname_and_age():
    return dal.get_employees_by_lastname_and_age()