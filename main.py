from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

@app.get('/blog')
def index(limit=10, published : bool = True, sort: Optional[str] = None):
    if published:
        return {'data':f'blog list of {limit}'}
    else:
        return {'data':f'{limit} blogs from the db'}
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpub'}

@app.get('/blog/{id}')
def show(id):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10): 
    return {'data':{'1','2'}}

class Blog (BaseModel):
    title:str
    body:str
    published_at:Optional[bool]

@app.post('blog')
def create_blog(blog:Blog):
    return {'data':f'created with title as{ blog.title}'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

