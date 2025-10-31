# importing libraries
from fastapi import FastAPI, Path, HTTPException, Query # path is used to enhance readability of paramter or add some data validation. 
import json

# first create object for fastapi
app = FastAPI()

# Helper Function for loading data (can be json, sql, or any other source)
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


# defining end points
@app.get("/") # defining paths
# definig funtion for end points
def hello():
    return {
        'message': 'Creating End to End API for Patients Data'
    }

# defining another endpoints
@app.get("/about")
def about():
    return {
        'message': 'This is about section'
    }

@app.get("/view")
def view():
    data = load_data()

    return data

# creating first path parameter route
@app.get("/patient/{patient_id}")   # here patient_id is the dynamic segment 
def view_patient(patient_id: str = Path(..., description='ID of the patient', example='P001')): # calling path function
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'Error': 'Patient not available'} #instead for returning this error we rasie HTTPExpection error with status code
    raise HTTPException(status_code=404, detail='Patient not found')

# Creating first endpoint using Query Paramter
@app.get('/sort')
def sort_patient(sort_by:str = Query(..., description='Sort on the basis of height, weight & bmi'), order: str = Query('asc', description='sort in asc or desc order') ):
    
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field selected from {valid_fields}') 
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid field selected between asc & desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

    


# for running code: uvicorn main:app --reload