
# what if we have to validate values on more then 1 field then, e.g if age is > 60 then emergecny contact also necessary in contact info this is depend on two fields then we use model validator.

from pydantic import BaseModel, EmailStr, model_validator, computed_field
from typing import Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    height: float
    weight: float
    martial_status: bool
    contact_info: Dict[str, str]

    # model validator
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_info:
            raise ValueError('Patient greater then age 60 must have emergency contact')
        return model
    
    # Lets discuss about computed field
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/self.height**2, 2) # when wiehgt is in KG & height in mtr
        return bmi # methond name will be called in print or as field name




def insert_data(patient= Patient):
    print(patient.name)
    print(patient.age)
    print('BMI', patient.bmi)

patient_info = {
    'name': 'Preet Kumar',
    'email': 'preet@jsbl.com',
    'age':63,
    'height': 1.6,
    'weight': 68,
    'martial_status': False,
    'contact_info': {'phone':'034343323', 'emergency':'45983492'}
}

p1 = Patient(**patient_info)

insert_data(p1)
