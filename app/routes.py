from fastapi import APIRouter
from typing import List,Dict,Any
from app import dal

router = APIRouter()


@router.get("/")
def get_engineering_high_salary_employees():
    pass
@router.get("/")
def get_employees_by_age_and_role():
    pass
@router.get("/")
def get_top_seniority_employees_excluding_hr():
    pass
@router.get("/")
def get_employees_by_age_or_seniority():
    pass
@router.get("/")
def get_managers_excluding_departments():
    pass
@router.get("/")
def get_employees_by_lastname_and_age():
    pass