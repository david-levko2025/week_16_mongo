from connection import collection


def get_engineering_high_salary_employees():
   query = collection.find(
        {'job_role.department':'Engineering','salary':{'$gt':65000}},
        {'_id':0,'employee_id':1,'name':1,'salary':1})

   return query

def get_employees_by_age_and_role():
    query = collection.find(
        {'$or':[
        {'job_role.title': 'Engineer'},
        {'job_role.title': 'Specialist'}]
        ,'age': {'$gte': 30}, 'age': {'$lte':45}}, {'_id':0})
    
    return query

def get_top_seniority_employees_excluding_hr():
    query = collection.find(
        {'department':{'$ne': 'HR'}}).sort('years_at_company',-1).limit(7)
    
    return query

def get_employees_by_age_or_seniority():
    query = collection.find(
        {{'$or': [{'age': {'$gt': 50}, 'years_at_company': {'$lt':3}}]}},
        {"_id":0,"employee_id":1,"name":1,"age":1,"years_at_company":1})
    
    return query

def get_managers_excluding_departments():
    query = collection.find(
        {'job_role.title':'Manager',
        'job_role.department':{'$nin': ['Sales', 'Marketing']},})
    
    return query

def get_employees_by_lastname_and_age():
    query = collection.find(
        {'name': {'$regex': ' Wright$'},
        'name': {'$regex': ' Nelson$'},
        'age': {'$lt': 35},},
        {
        '_id':0, 'name':1
        ,'age':1, 'job_role.department': 1}
    )
    return query