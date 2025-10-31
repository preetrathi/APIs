# creating a function where we are recieving patient data and then store in database

#  Problem 01: Type Validation
def pat_data_insersation(name: str, age: int):

    # to avoid insert of worng typed data we can strickly force e.g.
    # this is right approch but not sclable
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Inserted into database')
    else:
        raise TypeError('Incorrect data type')

pat_data_insersation('Preet', 32)
# actual function is made to insert the value string for name and int for age but a user can insert age as twenty-six this function also works for that it wil insert the wrong age formated value to database. which is we dont want. and this is the big failure.

# to avoid this I can use type hinting means defining the types of paramter in function then function hind will show the name is str and age is int but still by mistkaly if fucntion run with the age string value it will still insert the wrong formattted values. 


# Problem 2: Data Validation
def pat_data_insersation(name: str, age: int): # lets say age never by -ve to validate that data 
    # this script is doing both type vlaidation and data validation
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('Age cant be negative')
        else:
            print(name)
            print(age)
            print('Inserted into database')
    else:
        raise TypeError('Incorrect data type')

pat_data_insersation('Preet', -3)