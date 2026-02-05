from fastapi import APIRouter
import dal

router = APIRouter(prefix="/employees",tags=["Employees"])


@router.get("/engineering/high-salary")
def get_engineering_high_salary_employees():
    return dal.get_engineering_high_salary_employees() 

@router.get("/by-age-and-role")
def get_employees_by_age_and_role():
    return dal.get_employees_by_age_and_role()

@router.get("/top-seniority")
def get_top_seniority_employees_excluding_hr():
    return dal.get_top_seniority_employees_excluding_hr()

@router.get("/age-or-seniority")
def get_employees_by_age_or_seniority():
    return dal.get_employees_by_age_or_seniority()

@router.get("/managers/excluding-departments")
def get_managers_excluding_departments():
    return dal.get_managers_excluding_departments()

@router.get("/by-lastname-and-age")
def get_employees_by_lastname_and_age():
    return dal.get_employees_by_lastname_and_age()

@router.post("/uploadfile")
def upload_file():
    pass