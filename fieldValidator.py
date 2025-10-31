from pydantic import BaseModel, EmailStr, field_validator
from typing import List

class Patient(BaseModel):
    name:   str
    email:  EmailStr
    age:    int
    weight: float
    martial_status: bool

    #  for using field_validator, we need to create a methond inside our class and this method should be used with decorator
    # filed validator used to valid value on single field
    @field_validator('email') # we aslo tell on which field we are applying
    @classmethod # also tell this method is class method
    def email_validator(cls, value): # thn define our method takes two paramters class instance and the value of validator
        valid_domains = ['jsbl.com', 'hbl.com'] 
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    # also used for transformation 
    @field_validator('name')    # defauld mode is after
    @classmethod
    def trans_name(cls, value):
        return value.upper()
    
    #  field_validator operates on 2 modes, before & after mode




def data_inst(patient=Patient):
    print(patient.name)
    print(patient.email)


patient_info = {
    'name': 'Preet Kumar',
    'email': 'preet@jsbl.com',
    'age':32,
    'weight': 68,
    'martial_status': False
}

p1 = Patient(**patient_info) # validation perform at this step. type coerion

data_inst(p1)