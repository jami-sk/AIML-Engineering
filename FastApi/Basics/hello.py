from fastapi import FastAPI,Body, Header, Response

app = FastAPI()

@app.get("/hi")
def greet():
    return f"Hello Santosh"

@app.get("/hi/{who}")
def greet_new(who):
    return f"Hello {who}"

@app.get("/greet_param")
def greet_param(who):
    return f"Hello {who}"

@app.get("/greet_body")
def greet_body(who:str = Body(embed=True)):
    return f"Hello {who}"

@app.get("/greet_header")
def greet_header(who:str = Header()):
    return f"Hello {who}"

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name:str, value:str, response:Response):
    response.headers['name']=value
    return "normal body"

import datetime, pytest
from fastapi.encoders import jsonable_encoder
import json

@pytest.fixture
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)

def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    json_out = json.dumps(out)
    assert json_out

from FastApi.Basics.model.tag import Tag, TagIn, TagOut
import FastApi.Basics.service.tag as service

@app.post("/")
def create(tag_in:TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.utcnow(), secret="shhhhhh")
    service.create()
    return tag_in

@app.get('/{tag_str}', response_model=TagOut)
def get_one(tag_str:str) -> TagOut:
    tag: Tag = service.get(tag_str)
    return tag #even though we are return tag object but response model converts it to TagOut




if __name__=="__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)