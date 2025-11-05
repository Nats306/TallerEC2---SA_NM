from fastapi import FastAPI, HTTPException, status
from schemas import Persona
from aws import uploadPerson, countFiles
import botocore.exceptions

app = FastAPI()

@app.post("/personas/", status_code=status.HTTP_201_CREATED)
def upload_persona(persona: Persona):
    
    try: 
        uploadPerson(persona)

        total_files = countFiles()

        return  {
                "message": f"Persona '{persona.nombre} {persona.apellido}' uploaded successfully.",
                "total_files_in_bucket": total_files
            }
    except ValueError as e:
        raise HTTPException(
            status_code =400, #bad request
            detail=str(e)
        )
    
    except botocore.exceptions.ClientError as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"Error cargando la persona a s3: {e.response['Error']}"
            )
    
