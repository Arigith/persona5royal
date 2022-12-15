# Required imports
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware
import models, schemas, boto3

# Check and create database if not created already
models.Base.metadata.create_all(engine)

# What we are calling the app when running
app=FastAPI()

# Making so my frontend will have access to pull data from local and AWS
origins = [
    # local website address
    "http://localhost:3000",
    # local fastAPI address
    "http://127.0.0.1:8000",
    # AWS address
]

# Requirements to allow frontend to access data
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ec2 = boto3.client('ec2')

# request to show all persona 
@app.get('/list_all', response_model=list[schemas.PersonaBase])
def list_all(
    db:Session=Depends(get_db)
    ):
    persona=db.query(models.Persona).all()
    return persona

# request to add a persona to the database
@app.post('/add_persona', status_code=status.HTTP_201_CREATED)
def add_persona(request:schemas.PersonaBase, db:Session=Depends(get_db)):
    new_persona=models.Persona(arcana=request.arcana, persona_name=request.persona_name, starting_level=request.starting_level)
    db.add(new_persona)
    db.commit()
    db.refresh(new_persona)
    return new_persona

@app.get("/ec2")
def list_ec2():
    instance_list = []
    # List running instances
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Print the instance ID and other metadata
            inst = {}
            inst["instance_id"] = instance['InstanceId']
            inst["instance_type"] = instance['InstanceType']
            inst["instance_image_id"] = instance['ImageId']
            inst["instance_vpc_id"] = instance['VpcId']
            inst["instance_subnet_id"] = instance['SubnetId']
            inst["instance_security_groups"] = instance['SecurityGroups'][0]['GroupName']
            inst["instance_key_pair_name"] = instance['KeyName']
            instance_list.append(inst)
    return instance_list