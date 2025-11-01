
# Serialization: exporting our pydantic model as dictionary or jSON structure, it gives us builtin method by using them we can export our pydantic model as dic or json, many use cases as: debugging, api creation, logging
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str = 'Male'
    address: Address 
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


#  for exporing pydantic model as dict / json
p1_model_dict = p1.model_dump() # convert our pydantic model into dict
print(p1_model_dict)
print(type(p1_model_dict))

#  for json
p1_model_dict = p1.model_dump_json(include=['name','address']) # here we have flexibility to export specific fields by using include and exclude
print(p1_model_dict)
print(type(p1_model_dict))

#  other way of include
p1_model_dict = p1.model_dump_json(include={'name': True, 'address':{'city'}}) # here we have flexibility to export specific fields
print(p1_model_dict)
print(type(p1_model_dict))

# here is nanother parameter name as exclude_unset will not get default valeus of any object means at the type of export will not take those values which are not set

#  other way of include
p1_model_dict = p1.model_dump(exclude_unset=True) # here we have flexibility to export specific fields
print(p1_model_dict)
print(type(p1_model_dict))