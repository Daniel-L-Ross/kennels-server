from animals import request


EMPLOYEES = [
    {
        "id": 2,
        "name": "April Ludgate Dwyer",
        "locationId": 3,
    },
    {
        "id": 3,
        "name": "Donna Meagle",
    },
    {
        "id": 4,
        "name": "Andy Dwyer",
        "locationId": 2
    },
    {
        "name": "Steve",
        "locationId": 1,
        "id": 5
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
            break

    return requested_employee
