from pydantic import BaseModel

class Persona(BaseModel):
    nombre:str
    apellido:str
    edad:str
    cedula:str
    ciudad:str

