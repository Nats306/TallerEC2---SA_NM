import boto3
import json 
import botocore.exceptions
from schemas import Persona

def uploadPerson(person: Persona):

    s3 = boto3.client('s3')
    bucket_name = 'bucket-sofia-nati'
    file_name = f"{person.cedula}.json"

    try:
        s3.head_object(Bucket=bucket_name, Key=file_name) # si esto no levanta una excepción es porque el archivo existe, por ende levantamos una excepción de que el archivo con esta cedula ya existe 
        raise ValueError(f"Ya existe una persona con la cedula {person.cedula} en el bucket")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] != '404': #el error 404 significa que el archivo no existe, por ende esta bien que se cree
            raise e

    item_json = json.dumps(person.model_dump())

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=item_json,
        ContentType='application/json'
    )

def countFiles():
    s3 = boto3.client('s3')
    bucket_name = 'bucket-sofia-nati'

    response = s3.list_objects_v2(Bucket = bucket_name)

    if 'Contents' not in response:
        return 0
    
    count = len(response['Contents'])
    return count
