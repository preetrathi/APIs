
# using one model as a field in 2nd model
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address  # here for address I use a new pydantic model and use that pydantic model as field in other models becuase address is complex data type

address_dic = {
    'city': 'Karachi',
    'state': 'Sindh',
    'pin': '75435'
}

add_1 = Address(**address_dic)

patient_info = {
    'name': 'Preet Kumar',
    'age': 26,
    'gender': 'male',
    'address': add_1
}

p1 = Patient(**patient_info)

print(p1)
print(p1.name)
print(p1.address.city)
print(p1.address.pin)

#  benifit of using nested pydantic mode
    # Better organization of related data, (e.g vitals, address, insurance)
    # Readability: Easir for developers and API consumers to understand
    # Validation: nested model are validated automatically, no extra work needed
    # reusability: use vitals and address at multiple itme or in multiple models