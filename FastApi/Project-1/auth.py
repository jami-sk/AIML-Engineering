import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security: HTTPBasicCredentials = HTTPBasic()

secret_user: str = "admin"
secret_password: str = "Bhasa@123"

@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(security)) -> dict:
    """Get the username of the authenticated user"""
    if creds.username != secret_user or creds.password != secret_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return {"username": creds.username, "password": creds.password}

if __name__ == "__main__":
    uvicorn.run("auth:app", reload=True)