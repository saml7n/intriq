import time
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
import secrets
import base64

app = FastAPI()

class Document(BaseModel):
    id: str
    name: str
    type: str
    dataURL: Optional[str]
    triplet_id: Optional[List[str]]
    embedding_id: Optional[List[str]]

class Company(BaseModel):
    id: int
    name: str
    type: str
    sector: str
    valuation: int
    kpi: str
    goal: str
    triplet_id: Optional[List[str]]
    embedding_id: Optional[List[str]]

class Triplet(BaseModel):
    id: str
    subject: str
    relation: str
    object: str

class Embedding(BaseModel):
    id: str
    content: str
    vector: List[float]

class Node(BaseModel):
    id: str
    type: str
    position: dict
    label: str
    triplet_id: str

companies : dict[Company] = dict()
documents : dict[Document] = dict()

def decode_base64_from_dataurl(dataurl: str) -> tuple[bytes, str]:
    extension, data = dataurl.split(';base64,')
    extension = extension.split('/')[-1]
    return base64.b64decode(data), extension

def write_file_to_disk(
        source: bytes,
        id: str,
        file_extension: str) -> None:
    filename: str = (f'{id}.{file_extension}')
    with open(filename, 'wb') as file:
        file.write(source)

@app.post("/document")
def create_document(document: Document) -> str:
    id = str(uuid4())
    documents[id] = Document(id=id, name=document.name, type=document.type, dataURL=document.dataURL, triplet_id=None, embedding_id=None)
    src, ext = decode_base64_from_dataurl(document.dataURL)
    write_file_to_disk(src, id, ext)
    return id

@app.get("/documents")
def read_documents() -> List[Document]:
    print(len(documents))
    return [Document(id=x.id, type=x.type, name=x.name, dataURL=None, embedding_id=None, triplet_id=None) for x in documents.values()]

@app.get("/document/{id}")
def read_document(id: str) -> Document:
    if (id in documents.keys()):
        return documents[id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/document/{id}/blob")
def read_document_blob(id: str):
    # Your code here
    pass

@app.post("/company")
def create_company(company: Company) -> int:
    id = 1
    companies[id] = company
    return id

@app.put("/company")
def update_company(company: Company):
    # Your code here
    pass

@app.get("/company/{id}")
def read_company(id: int) -> Company:
    time.sleep(2)
    if (id in companies.keys()):
        return companies[id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/triplet/{id}")
def read_triplet(id: str):
    # Your code here
    pass

@app.get("/nodes")
def read_nodes():
    # Your code here
    pass

@app.put("/node/{id}")
def update_node(id: str, position: dict):
    # Your code here
    pass
