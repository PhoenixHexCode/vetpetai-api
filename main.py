from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

class Question(BaseModel):
    question : str

app = FastAPI()

@app.get('/')
def read_root():
    return {'response': 'Hello World'}

@app.post('/question')
async def question_response(request: Question):
    return request.question

handler = Mangum(app)

