from lecture_32_pydantic_models import Employee, CustomEmployee

basis_employee = Employee(
    name="Chris DeTuma",
    email="cdetuma@example.com",
    date_of_birth="1998-04-02",
    salary=123_000.00,
    department="IT",
    elected_benefits=True,
)

print(basis_employee)

# WRONG
# basis_employee = Employee(
#     employee_id=123,
#     name=False,
#     email="cdetumaexample.com",
#     date_of_birth="1998-0402",
#     salary="123_000.00",
#     department="PM",
#     elected_benefits=300,
# )

new_employee_dict = {
    "name": "Chris DeTuma",
    "email": "cdetuma@example.com",
    "date_of_birth": "1998-04-02",
    "salary": 123_000.00,
    "department": "IT",
    "elected_benefits": True,
}
print(Employee.model_validate(new_employee_dict))

new_employee_json = """
 {"employee_id":"d2e7b773-926b-49df-939a-5e98cbb9c9eb",
 "name":"Eric Slogrenta",
 "email":"eslogrenta@example.com",
 "date_of_birth":"1990-01-02",
 "salary":125000.0,
 "department":"HR",
 "elected_benefits":false}
 """
new_employee = Employee.model_validate_json(new_employee_json)
print(new_employee.model_dump())
print(new_employee.model_dump_json())
print(Employee.model_json_schema())

incorrect_employee_data = {
    "name": "",
    "email": "cdetuma@fakedomain.com",
    "birth_date": "1998-04-02",
    "salary": -10,
    "department": "IT",
    "elected_benefits": True,
}
custom_employee = CustomEmployee.model_validate(incorrect_employee_data)
