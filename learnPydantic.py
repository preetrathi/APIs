# pydantic 2 written in rust and much faster

# first we will create our pydantic mode in which we create schema of our data for that import basemodel whihc will be necessary whenever working with pydantic

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

#  by using Annotated and Field we can attach meta data.

# then we create a class, and makesure this will import baseclass. then this class will be made as pydantic model.
class Patient(BaseModel):  # Step: 01
    # in this class we define the ideal schema 
    # by default all fields are required which we defined in our mode. but some time we may define all field in schema but use some of them then what to do? then wo put some fields required and some optional.
    name: Annotated[str, Field(max_length=50, title='Name of Patient', description='Please keep the name less then 50 characters', examples=['Preet', 'Raj', 'Ali'])]           # str = Field(max_length=50)  # this is type validation, annotated field
    linkedin_url: AnyUrl
    email: EmailStr # here we used pydantic data validation built in data type
    age: int = Field(gt=17, lt=60)
    weight: Annotated[float, Field(gt=0, strict=True)] # here strict use to not allow type conversion # float = Field(gt=0)
    martial_status: Annotated[bool, Field(default=False, description='Martial Status True or False' )]  # Optional[bool] = False # We can set other field defualt values as well 
    allergies: Optional[List[str]] = None # we put that field as optional and adding default value as None
    contact_details: Dict[str, str]

    # Here we done with Type validation, now move towards data validation.
    # Pydantic gives its builtin data type of data validation e.g. EmailStr, AnyURL
    # We can also made our own custom data validation. by using pydantic function Field, this function is not only used for data validation but it has also a purpsoe to attach meta data. 
    # another important concept of FIeld validator: use for business use case data validation

# then send our pydantic object to our function or codebase
def inst_pat_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('data inserted')


patient_info = {'name': 'Preet Kumar', 'email': 'foj@gmail.com', 'age': 26, 'weight': 68.4, 'martial_status': False, 'allergies':['dust', 'pollen'], 'contact_details': {'phone':'239340395' } }

# then we instantiate our pydnatic class object
p1 = Patient(**patient_info) # unpack dict    # Step: 02

inst_pat_data(p1)

